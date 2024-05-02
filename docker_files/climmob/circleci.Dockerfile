FROM ubuntu:22.04

MAINTAINER Alliance Bioversity-CIAT
ENV CR=America/Costa_Rica
ENV DEBIAN_FRONTEND noninteractive
RUN ln -snf /usr/share/zoneinfo/$CR /etc/localtime && echo $CR > /etc/timezone
RUN apt-get update && apt-get -y upgrade && apt-get install -y software-properties-common && add-apt-repository universe && add-apt-repository multiverse

RUN apt-get install -y wget tzdata

# R
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
RUN add-apt-repository -y 'deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/'

RUN wget http://archive.ubuntu.com/ubuntu/pool/main/i/icu/libicu66_66.1-2ubuntu2_amd64.deb && dpkg -i ./libicu66_66.1-2ubuntu2_amd64.deb

# Mongo
RUN wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc |  gpg --dearmor | tee /usr/share/keyrings/mongodb.gpg > /dev/null
RUN echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/6.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-6.0.list

RUN apt-get update

RUN apt-get install -y build-essential qtbase5-dev qtbase5-private-dev qtdeclarative5-dev libqt5sql5-mysql libqt5webkit5-dev libqt5svg5-dev libqt5xmlpatterns5-dev cmake mongodb-org nano jq libboost-all-dev unzip zlib1g-dev automake npm redis-server libmysqlclient-dev git python3-venv texlive-extra-utils r-base libcurl4-openssl-dev pandoc pandoc-citeproc libfontconfig1-dev libcairo2-dev libudunits2-dev libgdal-dev xvfb sqlite3 libqt5sql5-sqlite libgmp3-dev libmpfr-dev tidy golang-go mysql-client-8.0 openjdk-17-jre-headless

# ---------------From Circle CI
# make Apt non-interactive
RUN echo 'APT::Get::Assume-Yes "true";' > /etc/apt/apt.conf.d/90circleci \
  && echo 'DPkg::Options "--force-confnew";' >> /etc/apt/apt.conf.d/90circleci


# Debian Jessie is EOL'd and original repos don't work.
# Switch to the archive mirror until we can get people to
# switch to Stretch.
RUN if grep -q Debian /etc/os-release && grep -q jessie /etc/os-release; then \
	rm /etc/apt/sources.list \
    && echo "deb http://archive.debian.org/debian/ jessie main" >> /etc/apt/sources.list \
    && echo "deb http://security.debian.org/debian-security jessie/updates main" >> /etc/apt/sources.list \
	; fi

# Make sure PATH includes ~/.local/bin
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=839155
# This only works for root. The circleci user is done near the end of this Dockerfile
RUN echo 'PATH="$HOME/.local/bin:$PATH"' >> /etc/profile.d/user-local-path.sh

# man directory is missing in some base images
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=863199
RUN apt-get update \
  && mkdir -p /usr/share/man/man1 \
  && apt-get install -y \
    git mercurial xvfb apt \
    locales sudo openssh-client ca-certificates tar gzip parallel \
    net-tools netcat unzip zip bzip2 gnupg curl wget make


# Set timezone to UTC by default
RUN ln -sf /usr/share/zoneinfo/Etc/UTC /etc/localtime

# Use unicode
RUN locale-gen C.UTF-8 || true
ENV LANG=C.UTF-8

# install jq
RUN JQ_URL="https://circle-downloads.s3.amazonaws.com/circleci-images/cache/linux-amd64/jq-latest" \
  && curl --silent --show-error --location --fail --retry 3 --output /usr/bin/jq $JQ_URL \
  && chmod +x /usr/bin/jq \
  && jq --version

# Install Docker

# Docker.com returns the URL of the latest binary when you hit a directory listing
# We curl this URL and `grep` the version out.
# The output looks like this:

#>    # To install, run the following commands as root:
#>    curl -fsSLO https://download.docker.com/linux/static/stable/x86_64/docker-17.05.0-ce.tgz && tar --strip-components=1 -xvzf docker-17.05.0-ce.tgz -C /usr/local/bin
#>
#>    # Then start docker in daemon mode:
#>    /usr/local/bin/dockerd

RUN set -ex \
  && export DOCKER_VERSION=$(curl --silent --fail --retry 3 https://download.docker.com/linux/static/stable/x86_64/ | grep -o -e 'docker-[.0-9]*\.tgz' | sort -r | head -n 1) \
  && DOCKER_URL="https://download.docker.com/linux/static/stable/x86_64/${DOCKER_VERSION}" \
  && echo Docker URL: $DOCKER_URL \
  && curl --silent --show-error --location --fail --retry 3 --output /tmp/docker.tgz "${DOCKER_URL}" \
  && ls -lha /tmp/docker.tgz \
  && tar -xz -C /tmp -f /tmp/docker.tgz \
  && mv /tmp/docker/* /usr/bin \
  && rm -rf /tmp/docker /tmp/docker.tgz \
  && which docker \
  && (docker version || true)

# docker compose
RUN COMPOSE_URL="https://circle-downloads.s3.amazonaws.com/circleci-images/cache/linux-amd64/docker-compose-latest" \
  && curl --silent --show-error --location --fail --retry 3 --output /usr/bin/docker-compose $COMPOSE_URL \
  && chmod +x /usr/bin/docker-compose \
  && docker-compose version

# install dockerize
RUN DOCKERIZE_URL="https://circle-downloads.s3.amazonaws.com/circleci-images/cache/linux-amd64/dockerize-latest.tar.gz" \
  && curl --silent --show-error --location --fail --retry 3 --output /tmp/dockerize-linux-amd64.tar.gz $DOCKERIZE_URL \
  && tar -C /usr/local/bin -xzvf /tmp/dockerize-linux-amd64.tar.gz \
  && rm -rf /tmp/dockerize-linux-amd64.tar.gz \
  && dockerize --version

RUN groupadd --gid 3434 circleci \
  && useradd --uid 3434 --gid circleci --shell /bin/bash --create-home circleci \
  && echo 'circleci ALL=NOPASSWD: ALL' >> /etc/sudoers.d/50-circleci \
  && echo 'Defaults    env_keep += "DEBIAN_FRONTEND"' >> /etc/sudoers.d/env_keep

# BEGIN IMAGE CUSTOMIZATIONS

# Install pipenv and poetry
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3 get-pip.py
RUN sudo pip install --no-cache pipenv poetry
RUN sudo pip uninstall --yes setuptools
RUN sudo pip install setuptools==57.5.0
# END IMAGE CUSTOMIZATIONS
# -------------------------------

# This is a patched MySQL Driver to allow connections between Client 8.0 and Server 5.7.X
# COPY ./docker_files/sqldriver/libqsqlmysql.s_o /usr/lib/x86_64-linux-gnu/qt5/plugins/sqldrivers/libqsqlmysql.so
# Firefox
RUN apt-get install -y libdbus-glib-1-2 libgtk2.0-0

RUN wget -O ~/Firefox.tar.bz2 "https://download.mozilla.org/?product=firefox-latest&os=linux64"
RUN tar xjf ~/Firefox.tar.bz2 -C /opt/

RUN ln -s /opt/firefox/firefox /usr/bin/

#RUN echo "export MOZ_HEADLESS=1" >> /etc/bash.bashrc

# MySQL Shell
RUN wget https://dev.mysql.com/get/mysql-apt-config_0.8.24-1_all.deb
RUN dpkg -i ./mysql-apt-config_0.8.24-1_all.deb

RUN apt-get update

RUN apt-get install -y mysql-shell

# Svg2png
RUN npm install svg2png -g --unsafe-perm

# Json2csv
RUN npm install -g json2csv

#WebKit's
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz
RUN tar xvfz geckodriver-v0.31.0-linux64.tar.gz && cp geckodriver /bin

#ODKTOOLS
RUN wget https://github.com/BurntSushi/xsv/releases/download/0.13.0/xsv-0.13.0-x86_64-unknown-linux-musl.tar.gz
RUN tar xvfz xsv-0.13.0-x86_64-unknown-linux-musl.tar.gz && cp xsv /bin

RUN git clone https://github.com/qlands/csv2xlsx.git
WORKDIR csv2xlsx
RUN go build && cp csv2xlsx /bin

WORKDIR /opt
RUN mkdir odktools-deps
RUN git clone https://github.com/qlands/odktools.git -b stable-2.4

WORKDIR /opt/odktools-deps
RUN wget https://github.com/mongodb/mongo-c-driver/releases/download/1.21.1/mongo-c-driver-1.21.1.tar.gz
RUN wget https://github.com/mongodb/mongo-cxx-driver/releases/download/r3.6.7/mongo-cxx-driver-r3.6.7.tar.gz
RUN wget https://github.com/jmcnamara/libxlsxwriter/archive/refs/tags/RELEASE_1.1.4.tar.gz
RUN wget https://github.com/stachenov/quazip/archive/refs/tags/v1.3.tar.gz
RUN git clone https://github.com/rgamble/libcsv.git

RUN tar xvfz mongo-c-driver-1.21.1.tar.gz
WORKDIR /opt/odktools-deps/mongo-c-driver-1.21.1
RUN mkdir build_here
WORKDIR /opt/odktools-deps/mongo-c-driver-1.21.1/build_here
RUN cmake ..
RUN make
RUN make install
WORKDIR /opt/odktools-deps

RUN tar xvfz mongo-cxx-driver-r3.6.7.tar.gz
WORKDIR /opt/odktools-deps/mongo-cxx-driver-r3.6.7
RUN mkdir build_here
WORKDIR /opt/odktools-deps/mongo-cxx-driver-r3.6.7/build_here
RUN cmake -DCMAKE_C_FLAGS:STRING="-O2 -fPIC" -DCMAKE_CXX_FLAGS:STRING="-O2 -fPIC" -DBSONCXX_POLY_USE_BOOST=1 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local ..
RUN make
RUN make install
WORKDIR /opt/odktools-deps

RUN tar xvfz v1.3.tar.gz
WORKDIR /opt/odktools-deps/quazip-1.3
RUN mkdir build
WORKDIR /opt/odktools-deps/quazip-1.3/build
RUN cmake -DCMAKE_C_FLAGS:STRING="-fPIC" -DCMAKE_CXX_FLAGS:STRING="-fPIC" ..
RUN make
RUN make install
WORKDIR /opt/odktools-deps

RUN ln -s /usr/bin/aclocal-1.16 /usr/bin/aclocal-1.14 && ln -s /usr/bin/automake-1.16 /usr/bin/automake-1.14

RUN tar xvfz RELEASE_1.1.4.tar.gz
WORKDIR /opt/odktools-deps/libxlsxwriter-RELEASE_1.1.4
RUN mkdir build
WORKDIR /opt/odktools-deps/libxlsxwriter-RELEASE_1.1.4/build
RUN cmake ..
RUN make
RUN make install
WORKDIR /opt/odktools-deps

WORKDIR /opt/odktools-deps/libcsv
RUN ./configure
RUN make
RUN make install

WORKDIR /opt/odktools

RUN qmake
RUN make

WORKDIR /opt
RUN git clone https://github.com/BioversityCostaRica/wkhtmltopdf.git
WORKDIR wkhtmltopdf
RUN qmake
RUN make -j 4
RUN make install

WORKDIR /opt
RUN git clone https://github.com/AgrDataSci/ClimMob-analysis.git new_r_code

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y locales \
    && sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && dpkg-reconfigure --frontend=noninteractive locales \
    && update-locale LANG=en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

#COPY ./docker_files/packages.r /opt
WORKDIR /opt
#RUN Rscript ./new_r_code/R/check_packages.R
#RUN Rscript ./packages.r
RUN mkdir climmob_repository
RUN mkdir climmob_log
RUN mkdir climmob_celery
RUN mkdir climmob_gunicorn
RUN mkdir climmob_config
RUN mkdir climmob_plugins

RUN chown -R circleci /opt/climmob_repository
RUN chown -R circleci /opt/climmob_log
RUN chown -R circleci /opt/climmob_celery
RUN chown -R circleci /opt/climmob_gunicorn
RUN chown -R circleci /opt/climmob_config
RUN chown -R circleci /opt/climmob_plugins

RUN ldconfig
USER circleci
ENV PATH /home/circleci/.local/bin:/home/circleci/bin:${PATH}

CMD ["/bin/bash"]
import configparser
import logging
import os
import sys

from jinja2 import Environment, FileSystemLoader

log = logging.getLogger("climmob")


def usage(argv):
    cmd = os.path.basename(argv[0])
    print(
        "usage: %s <path_to_ini_file> <path_to_climmob> \n"
        "(example: %s ./development.ini .)" % (cmd, cmd)
    )
    sys.exit(1)


def get_ini_value(ini_file, key, default=None):
    try:
        config = configparser.ConfigParser()
        config.read(ini_file)
        return config.get("app:climmob", key)
    except Exception as e:
        log.warning(
            "Warning: Unable to find key {}. {} . Default used".format(key, str(e))
        )
        return default


def main(argv=sys.argv):
    if len(argv) != 3:
        usage(argv)
    if not os.path.exists(os.path.abspath(argv[1])):
        print("Ini file does not exists")
        sys.exit(1)
    if not os.path.exists(os.path.abspath(argv[2])):
        print("Path to climmob does not exits")
        sys.exit(1)

    climmob_ini_file_path = os.path.abspath(argv[1])
    climmob_path = os.path.abspath(argv[2])

    alembic_ini_file = os.path.join(climmob_path, *["alembic.ini"])

    template_environment = Environment(
        autoescape=False,
        loader=FileSystemLoader(os.path.join(climmob_path, "templates")),
        trim_blocks=False,
    )
    sqlalchemy_url = get_ini_value(os.path.abspath(argv[1]), "sqlalchemy.url", "empty")
    context = {
        "sqlalchemy_url": sqlalchemy_url,
        "climmob_ini_file": climmob_ini_file_path,
    }

    rendered_template = template_environment.get_template("alembic.jinja2").render(
        context
    )

    with open(alembic_ini_file, "w") as f:
        f.write(rendered_template)

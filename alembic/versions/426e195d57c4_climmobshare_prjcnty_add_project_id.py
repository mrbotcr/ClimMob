"""climmobShare - Prjcnty - add project_id

Revision ID: 426e195d57c4
Revises: e8be0af780e1
Create Date: 2021-08-03 16:16:14.215529

"""
import sqlalchemy as sa
from sqlalchemy.orm.session import Session

from alembic import op

# revision identifiers, used by Alembic.
revision = "426e195d57c4"
down_revision = "e8be0af780e1"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "prjcnty", sa.Column("project_id", sa.Unicode(length=64), nullable=True)
    )

    session = Session(bind=op.get_bind())
    try:
        projects = session.execute("Select * from project")
        for project in projects:
            session.execute(
                "UPDATE prjcnty SET project_id = '"
                + project.project_id
                + "' WHERE (user_name = '"
                + project.user_name
                + "') and (project_cod = '"
                + project.project_cod
                + "');"
            )
    except Exception as e:
        print(str(e))
        exit(1)

    session.commit()
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("prjcnty", "project_id")
    # ### end Alembic commands ###

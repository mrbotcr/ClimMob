"""add_country_to_project

Revision ID: 771d039833d4
Revises: 3f2fa668dbac
Create Date: 2020-03-17 16:09:15.022826

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "771d039833d4"
down_revision = "3f2fa668dbac"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "project", sa.Column("project_cnty", sa.String(length=3), nullable=True)
    )
    op.create_index(
        op.f("ix_project_project_cnty"), "project", ["project_cnty"], unique=False
    )
    op.create_foreign_key(
        op.f("fk_project_project_cnty_country"),
        "project",
        "country",
        ["project_cnty"],
        ["cnty_cod"],
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        op.f("fk_project_project_cnty_country"), "project", type_="foreignkey"
    )
    op.drop_index(op.f("ix_project_project_cnty"), table_name="project")
    op.drop_column("project", "project_cnty")
    # ### end Alembic commands ###

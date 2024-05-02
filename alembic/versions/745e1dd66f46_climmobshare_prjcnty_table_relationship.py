"""climmobShare - Prjcnty - table relationship

Revision ID: 745e1dd66f46
Revises: 9318991f04ab
Create Date: 2021-08-10 13:57:05.335048

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = "745e1dd66f46"
down_revision = "9318991f04ab"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("PRIMARY", "prjcnty", type_="primary")
    op.create_primary_key("pk_prjcnty", "prjcnty", ["project_id", "cnty_cod"])

    op.create_foreign_key(
        op.f("fk_prjcnty_project_id_project"),
        "prjcnty",
        "project",
        ["project_id"],
        ["project_id"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        op.f("fk_prjcnty_cnty_cod_country"),
        "prjcnty",
        "country",
        ["cnty_cod"],
        ["cnty_cod"],
        ondelete="CASCADE",
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("PRIMARY", "prjcnty", type_="primary")
    op.create_primary_key(
        "pk_prjcnty", "prjcnty", ["user_name", "project_cod", "cnty_cod"]
    )

    op.drop_constraint(
        op.f("fk_prjcnty_cnty_cod_country"), "prjcnty", type_="foreignkey"
    )
    op.drop_constraint(
        op.f("fk_prjcnty_project_id_project"), "prjcnty", type_="foreignkey"
    )

    # ### end Alembic commands ###

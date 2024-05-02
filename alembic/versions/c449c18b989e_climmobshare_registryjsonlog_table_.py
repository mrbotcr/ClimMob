"""climmobShare - RegistryJsonLog - table relationship

Revision ID: c449c18b989e
Revises: 314451ce468b
Create Date: 2021-08-10 11:09:45.467773

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = "c449c18b989e"
down_revision = "314451ce468b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("PRIMARY", "registry_jsonlog", type_="primary")
    op.create_primary_key("pk_project", "registry_jsonlog", ["project_id", "log_id"])

    op.create_foreign_key(
        op.f("fk_registry_jsonlog_enum_user_enumerator"),
        "registry_jsonlog",
        "enumerator",
        ["enum_user", "enum_id"],
        ["user_name", "enum_id"],
    )
    op.create_foreign_key(
        op.f("fk_registry_jsonlog_project_id_project"),
        "registry_jsonlog",
        "project",
        ["project_id"],
        ["project_id"],
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("PRIMARY", "registry_jsonlog", type_="primary")
    op.create_primary_key(
        "pk_project", "registry_jsonlog", ["user_name", "project_cod", "log_id"]
    )

    op.drop_constraint(
        op.f("fk_registry_jsonlog_project_id_project"),
        "registry_jsonlog",
        type_="foreignkey",
    )
    op.drop_constraint(
        op.f("fk_registry_jsonlog_enum_user_enumerator"),
        "registry_jsonlog",
        type_="foreignkey",
    )
    # ### end Alembic commands ###

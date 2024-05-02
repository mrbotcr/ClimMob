"""climmobShare - Registry - Remove user_name and project_cod

Revision ID: 1d20c409a2f8
Revises: 5fe2394889c0
Create Date: 2021-08-19 13:46:56.653914

"""
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

from alembic import op

# revision identifiers, used by Alembic.
revision = "1d20c409a2f8"
down_revision = "5fe2394889c0"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("registry", "user_name")
    op.drop_column("registry", "project_cod")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "registry", sa.Column("project_cod", mysql.VARCHAR(length=80), nullable=False)
    )
    op.add_column(
        "registry", sa.Column("user_name", mysql.VARCHAR(length=80), nullable=False)
    )
    # ### end Alembic commands ###

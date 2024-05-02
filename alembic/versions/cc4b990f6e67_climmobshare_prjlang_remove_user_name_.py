"""climmobShare - Prjlang - Remove user_name and project_cod

Revision ID: cc4b990f6e67
Revises: 3946605a6354
Create Date: 2021-08-18 14:04:44.185054

"""
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

from alembic import op

# revision identifiers, used by Alembic.
revision = "cc4b990f6e67"
down_revision = "3946605a6354"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("prjlang", "user_name")
    op.drop_column("prjlang", "project_cod")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "prjlang", sa.Column("project_cod", mysql.VARCHAR(length=80), nullable=False)
    )
    op.add_column(
        "prjlang", sa.Column("user_name", mysql.VARCHAR(length=80), nullable=False)
    )

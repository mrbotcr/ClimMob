"""climmobShare - Products - Remove user_name and project_cod

Revision ID: 6efa7642db00
Revises: 49199d144454
Create Date: 2021-08-18 10:32:06.832180

"""
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

from alembic import op

# revision identifiers, used by Alembic.
revision = "6efa7642db00"
down_revision = "49199d144454"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("products", "user_name")
    op.drop_column("products", "project_cod")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "products", sa.Column("project_cod", mysql.VARCHAR(length=80), nullable=False)
    )
    op.add_column(
        "products", sa.Column("user_name", mysql.VARCHAR(length=80), nullable=False)
    )
    # ### end Alembic commands ###

"""product_id has primary key in table products

Revision ID: 8f9c1f3f2153
Revises: 811485b1d9b2
Create Date: 2021-07-14 08:58:43.052570

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = "8f9c1f3f2153"
down_revision = "811485b1d9b2"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("celery_taskid", "products", type_="primary")
    op.create_primary_key("pk_products", "products", ["celery_taskid", "product_id"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

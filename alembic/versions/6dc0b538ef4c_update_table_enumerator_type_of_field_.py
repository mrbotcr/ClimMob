"""Update table Enumerator type of field enum_password

Revision ID: 6dc0b538ef4c
Revises: 0056f2fe1256
Create Date: 2022-03-18 12:23:58.440573

"""
from sqlalchemy.dialects import mysql

from alembic import op

# revision identifiers, used by Alembic.
revision = "6dc0b538ef4c"
down_revision = "0056f2fe1256"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "enumerator",
        "enum_password",
        existing_type=mysql.VARCHAR(
            charset="utf8mb4", collation="utf8mb4_unicode_ci", length=80
        ),
        type_=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        existing_nullable=True,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "enumerator",
        "enum_password",
        existing_type=mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
        type_=mysql.VARCHAR(
            charset="utf8mb4", collation="utf8mb4_unicode_ci", length=80
        ),
        existing_nullable=True,
    )

    # ### end Alembic commands ###

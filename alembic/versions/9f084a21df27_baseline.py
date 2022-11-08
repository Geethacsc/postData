"""baseline

Revision ID: 9f084a21df27
Revises: 55477bfca79c
Create Date: 2022-11-08 15:20:04.800856

"""
from alembic import op
import sqlalchemy as sa
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, Integer, String

# revision identifiers, used by Alembic.
revision = '9f084a21df27'
down_revision = '55477bfca79c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'employee_data',
        Column('id', Integer, primary_key=True),
        Column('name', String),
        Column('position', String),
    )


def downgrade() -> None:
    op.drop_table('employee_data')

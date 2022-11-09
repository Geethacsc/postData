"""employee_data

Revision ID: 12e6f67b412e
Revises: 
Create Date: 2022-11-09 15:58:35.568786

"""
from alembic import op
from sqlalchemy import Column, Integer, String

# revision identifiers, used by Alembic.
revision = '12e6f67b412e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'employee',
        Column('id', Integer, primary_key=True),
        Column('name',String(50), nullable=False),
        Column('position',String)
    )

def downgrade() -> None:
    op.drop_table('employee')

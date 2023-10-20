"""Add_table_user

Revision ID: 4c599ef3ef75
Revises: 
Create Date: 2023-10-20 20:32:59.205669

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import datetime
from pyAPI.api.models.carModel import Car


# revision identifiers, used by Alembic.
revision: str = 'add_user_table'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Tabela User
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('surname', sa.String(length=255), nullable=False),
        sa.Column('year', sa.Integer(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('(now())'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Tabela Car
    op.create_table('cars',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('model', sa.String(length=255), nullable=False),
        sa.Column('brand', sa.String(length=255), nullable=False),
        sa.Column('year', sa.Integer(), nullable=False),
        sa.Column('value', sa.Float(), nullable=False),
        sa.Column('sold', sa.Boolean(), nullable=False),
        sa.Column('owners', sa.Integer(), nullable=False),
        sa.Column('buyer_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=True),
        sa.ForeignKeyConstraint(['buyer_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('users')
    op.drop_table('cars')

"""Add new columns and indexes

Revision ID: e62fd1f13cf2
Revises: 
Create Date: 2025-01-07 02:11:20.207613

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision = 'add_new_columns_and_indexes'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('trip', sa.Column('status', sa.String(length=20), nullable=True))
    op.add_column('car', sa.Column('color', sa.String(length=20), nullable=True))

    op.create_index('ix_trip_departure_date', 'trip', ['departure_date'])
    op.create_index('ix_car_number_brand', 'car', ['number', 'brand'])


def downgrade() -> None:
    op.drop_index('ix_trip_departure_date', table_name='trip')
    op.drop_index('ix_car_number_brand', table_name='car')

    op.drop_column('trip', 'status')
    op.drop_column('car', 'color')

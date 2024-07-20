"""add foreignkey to posts

Revision ID: 9a300c6b3c8f
Revises: d743d49fc182
Create Date: 2024-07-20 23:39:00.856222

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9a300c6b3c8f'
down_revision: Union[str, None] = 'd743d49fc182'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'posts',
        sa.Column('user_id', sa.Integer(), nullable=False)
    )
    op.create_foreign_key('posts_users_fkey', source_table='posts', referent_table='users', local_cols=['user_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fkey', table_name='posts')
    op.drop_column('posts', 'user_id')
    pass

"""add content column to posts

Revision ID: 1025c8e2a5cd
Revises: ad3c8b8c37f2
Create Date: 2024-07-20 23:27:27.976085

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1025c8e2a5cd'
down_revision: Union[str, None] = 'ad3c8b8c37f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', 
        sa.Column('content', sa.String(), nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass

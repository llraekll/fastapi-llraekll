"""add content column table to posts table

Revision ID: 322c3caca05e
Revises: 1a9e337fb361
Create Date: 2022-06-03 19:39:08.561542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '322c3caca05e'
down_revision = '1a9e337fb361'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass

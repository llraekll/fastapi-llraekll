"""complete posts table columns 

Revision ID: 6d3a217bc39c
Revises: 2ab79b4498af
Create Date: 2022-06-04 10:58:23.554931

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d3a217bc39c'
down_revision = '2ab79b4498af'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='True'),)
    op.add_column('posts',sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'),nullable=False),)
    pass


def downgrade():
    op.drop_column('posts', 'published',)
    op.drop_column('posts', 'created_at')
    pass

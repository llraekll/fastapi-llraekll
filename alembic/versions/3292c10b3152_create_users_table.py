"""create users table

Revision ID: 3292c10b3152
Revises: 322c3caca05e
Create Date: 2022-06-03 19:54:54.215847

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3292c10b3152'
down_revision = '322c3caca05e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), 
                            server_default=sa.text('now()'),nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass

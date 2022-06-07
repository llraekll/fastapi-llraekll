"""create posts table

Revision ID: 1a9e337fb361
Revises: 
Create Date: 2022-06-03 19:20:29.798942

"""
from tokenize import String
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a9e337fb361'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                            sa.Column("title", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass

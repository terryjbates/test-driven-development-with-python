"""Create items table

Revision ID: 31e132d1c3f5
Revises: 35a8c5b17aa2
Create Date: 2017-05-01 18:21:47.550004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31e132d1c3f5'
down_revision = '35a8c5b17aa2'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('items',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('text', sa.VARCHAR(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('items')


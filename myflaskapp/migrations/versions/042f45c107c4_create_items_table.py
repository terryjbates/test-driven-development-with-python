"""Create items table

Revision ID: 042f45c107c4
Revises: 8b1cf2bfda5e
Create Date: 2017-04-24 02:31:00.545797

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '042f45c107c4'
down_revision = '8b1cf2bfda5e'
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

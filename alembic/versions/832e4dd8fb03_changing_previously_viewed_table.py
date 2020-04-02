"""Changing previously viewed table

Revision ID: 832e4dd8fb03
Revises: 7fb65e9a32f6
Create Date: 2020-03-31 19:37:45.684485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '832e4dd8fb03'
down_revision = '7fb65e9a32f6'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('previously_recommended')
    op.create_table('previously_recommended',
                    sa.Column('profile_id', sa.String(length=255), nullable=True),
                    sa.Column('product_id', sa.String(length=255), nullable=True),
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['profile_id'], ['profiles.profile_id'],),
                    sa.ForeignKeyConstraint(['product_id'], ['products.product_id'],),
                    sa.PrimaryKeyConstraint('id'),
                    )


def downgrade():
    op.drop_table('previously_recommended')

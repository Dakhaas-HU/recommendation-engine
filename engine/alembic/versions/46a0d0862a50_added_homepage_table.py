"""Added homepage table

Revision ID: 46a0d0862a50
Revises: e82efd385587
Create Date: 2020-04-08 11:09:19.446505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46a0d0862a50'
down_revision = 'e82efd385587'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('homepage_recommendations',
    sa.Column('term_id', sa.Integer(), nullable=True),
    sa.Column('category', sa.String(length=255), nullable=True),
    sa.Column('product_ids', sa.Text(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['term_id'], ['trend_terms.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('homepage_recommendations')
    # ### end Alembic commands ###

"""Changed order to orders

Revision ID: bd054875c0a7
Revises: c3f212369cd5
Create Date: 2020-04-04 11:49:21.093911

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bd054875c0a7'
down_revision = 'c3f212369cd5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('session_id', sa.String(length=255), nullable=False),
    sa.Column('product_id', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.product_id'], ),
    sa.ForeignKeyConstraint(['session_id'], ['sessions.profile_id'], ),
    sa.PrimaryKeyConstraint('session_id')
    )
    op.drop_table('order')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('session_id', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('product_id', mysql.VARCHAR(length=255), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.product_id'], name='order_ibfk_1'),
    sa.ForeignKeyConstraint(['session_id'], ['sessions.profile_id'], name='order_ibfk_2'),
    sa.PrimaryKeyConstraint('session_id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.drop_table('orders')
    # ### end Alembic commands ###
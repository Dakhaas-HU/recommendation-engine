"""Added profiles

Revision ID: 9649e0606161
Revises: 6c073196c083
Create Date: 2020-03-24 15:16:52.347473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9649e0606161'
down_revision = '6c073196c083'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profiles',
    sa.Column('profile_id', sa.String(length=255), nullable=False),
    sa.Column('segment', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('profile_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profiles')
    # ### end Alembic commands ###

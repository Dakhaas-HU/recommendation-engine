"""Changed previously_recommended fk back to profile

Revision ID: c3f212369cd5
Revises: 08900a90d6a1
Create Date: 2020-04-02 13:24:58.812862

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c3f212369cd5'
down_revision = '08900a90d6a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('viewed_before', sa.Column('profile_id', sa.String(length=255), nullable=False))
    op.drop_constraint('viewed_before_ibfk_2', 'viewed_before', type_='foreignkey')
    op.create_foreign_key(None, 'viewed_before', 'profiles', ['profile_id'], ['profile_id'])
    op.drop_column('viewed_before', 'session_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('viewed_before', sa.Column('session_id', mysql.VARCHAR(length=255), nullable=False))
    op.drop_constraint(None, 'viewed_before', type_='foreignkey')
    op.create_foreign_key('viewed_before_ibfk_2', 'viewed_before', 'sessions', ['session_id'], ['session_id'])
    op.drop_column('viewed_before', 'profile_id')
    # ### end Alembic commands ###
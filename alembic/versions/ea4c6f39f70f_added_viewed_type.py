"""Added viewed type

Revision ID: ea4c6f39f70f
Revises: cd45de908f14
Create Date: 2020-03-24 17:11:58.784385

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea4c6f39f70f'
down_revision = 'cd45de908f14'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('viewed_type',
    sa.Column('session_id', sa.String(length=255), nullable=False),
    sa.Column('views', sa.Integer(), nullable=True),
    sa.Column('type_name', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['session_id'], ['sessions.profile_id'], ),
    sa.PrimaryKeyConstraint('session_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('viewed_type')
    # ### end Alembic commands ###
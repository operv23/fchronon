"""followers

Revision ID: 355bfb34acbf
Revises: 4b3aa1348f7e
Create Date: 2018-03-18 09:23:09.432713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '355bfb34acbf'
down_revision = '4b3aa1348f7e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###

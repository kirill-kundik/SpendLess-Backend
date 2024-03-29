"""added recommended challenge relation

Revision ID: 80f80413d24c
Revises: 118cfc734d6b
Create Date: 2019-11-16 16:01:36.530817

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80f80413d24c'
down_revision = '118cfc734d6b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recommended_challenges',
    sa.Column('challenge_fk', sa.Integer(), nullable=False),
    sa.Column('user_fk', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['challenge_fk'], ['challenge.id'], onupdate='CASCADE', ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['user_fk'], ['user.id'], onupdate='CASCADE', ondelete='CASCADE')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recommended_challenges')
    # ### end Alembic commands ###

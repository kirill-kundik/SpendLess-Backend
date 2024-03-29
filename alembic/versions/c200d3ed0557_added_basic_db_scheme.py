"""Added basic db scheme

Revision ID: c200d3ed0557
Revises: 
Create Date: 2019-11-15 23:20:57.910577

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c200d3ed0557'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('color', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sub_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('color', sa.String(length=10), nullable=True),
    sa.Column('period', sa.Enum('daily', 'weekly', 'monthly', 'half_yearly', 'yearly', name='periodtype'), nullable=True),
    sa.Column('category_fk', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_fk'], ['category.id'], onupdate='CASCADE', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Numeric(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('sub_category_fk', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['sub_category_fk'], ['sub_category.id'], onupdate='CASCADE', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('item')
    op.drop_table('sub_category')
    op.drop_table('category')
    # ### end Alembic commands ###

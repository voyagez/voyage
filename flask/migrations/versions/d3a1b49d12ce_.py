"""empty message

Revision ID: d3a1b49d12ce
Revises: a418372ae6a1
Create Date: 2023-08-31 14:20:24.769887

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3a1b49d12ce'
down_revision = 'a418372ae6a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rooms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('max_people', sa.Integer(), nullable=True),
    sa.Column('desc', sa.String(), nullable=True),
    sa.Column('room_numbers', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('hotels', schema=None) as batch_op:
        batch_op.add_column(sa.Column('hotel_type', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('city', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('address', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('distance', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('photo', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('title', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('desc', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('rating', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('cheapest_price', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('featured', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hotels', schema=None) as batch_op:
        batch_op.drop_column('featured')
        batch_op.drop_column('cheapest_price')
        batch_op.drop_column('rating')
        batch_op.drop_column('desc')
        batch_op.drop_column('title')
        batch_op.drop_column('photo')
        batch_op.drop_column('distance')
        batch_op.drop_column('address')
        batch_op.drop_column('city')
        batch_op.drop_column('hotel_type')

    op.drop_table('rooms')
    # ### end Alembic commands ###

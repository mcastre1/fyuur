"""empty message

Revision ID: 1e3fb91a6b5b
Revises: 793e5516d6e1
Create Date: 2023-02-26 20:43:47.402472

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e3fb91a6b5b'
down_revision = '793e5516d6e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('venu_name', sa.String(), nullable=False),
    sa.Column('artis_id', sa.Integer(), nullable=False),
    sa.Column('artist_name', sa.String(), nullable=False),
    sa.Column('artist_image_link', sa.String(), nullable=False),
    sa.Column('start_time', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Show')
    # ### end Alembic commands ###

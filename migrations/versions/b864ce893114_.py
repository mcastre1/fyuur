"""empty message

Revision ID: b864ce893114
Revises: 60cbeb1371b0
Create Date: 2023-02-26 21:22:50.460764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b864ce893114'
down_revision = '60cbeb1371b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shows',
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], ),
    sa.PrimaryKeyConstraint('venue_id', 'artist_id')
    )
    op.drop_table('Show')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Show',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Show_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('venue_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('venu_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('artis_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('artist_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('artist_image_link', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('start_time', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='Show_pkey')
    )
    op.drop_table('shows')
    # ### end Alembic commands ###

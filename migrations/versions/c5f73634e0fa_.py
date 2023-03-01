"""empty message

Revision ID: c5f73634e0fa
Revises: e069f3b32a03
Create Date: 2023-02-27 22:01:58.173498

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5f73634e0fa'
down_revision = 'e069f3b32a03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Artist', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('city',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.alter_column('state',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.alter_column('genres',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Artist', schema=None) as batch_op:
        batch_op.alter_column('genres',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('state',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('city',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###

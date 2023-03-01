"""empty message

Revision ID: 889aca3edf54
Revises: c5f73634e0fa
Create Date: 2023-02-27 22:17:38.531386

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '889aca3edf54'
down_revision = 'c5f73634e0fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Artist', schema=None) as batch_op:
        batch_op.alter_column('genres',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.Integer(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Artist', schema=None) as batch_op:
        batch_op.alter_column('genres',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=120),
               existing_nullable=False)

    # ### end Alembic commands ###

"""empty message

Revision ID: d597c2fc96f5
Revises: ea0a5719870b
Create Date: 2023-02-27 22:23:12.675496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd597c2fc96f5'
down_revision = 'ea0a5719870b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Artist', schema=None) as batch_op:
        batch_op.alter_column('genres',
               existing_type=sa.VARCHAR(length=500),
               type_=sa.Boolean(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Artist', schema=None) as batch_op:
        batch_op.alter_column('genres',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(length=500),
               existing_nullable=False)

    # ### end Alembic commands ###

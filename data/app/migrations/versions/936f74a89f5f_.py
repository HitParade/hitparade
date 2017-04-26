"""empty message

Revision ID: 936f74a89f5f
Revises: 6998bbd58cf9
Create Date: 2017-04-25 02:34:26.072729

"""

# revision identifiers, used by Alembic.
revision = '936f74a89f5f'
down_revision = '6998bbd58cf9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('player', 'state',
               existing_type=sa.VARCHAR(length=16),
               type_=sa.String(length=32),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('player', 'state',
               existing_type=sa.String(length=32),
               type_=sa.VARCHAR(length=16),
               existing_nullable=True)
    # ### end Alembic commands ###

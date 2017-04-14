"""empty message

Revision ID: 487c693132ab
Revises: 527057b05a8e
Create Date: 2017-04-14 14:47:45.908609

"""

# revision identifiers, used by Alembic.
revision = '487c693132ab'
down_revision = '527057b05a8e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('division', 'name',
               existing_type=sa.VARCHAR(length=21),
               type_=sa.String(length=36),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('division', 'name',
               existing_type=sa.String(length=36),
               type_=sa.VARCHAR(length=21),
               existing_nullable=True)
    # ### end Alembic commands ###

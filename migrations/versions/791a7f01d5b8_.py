"""empty message

Revision ID: 791a7f01d5b8
Revises: 
Create Date: 2020-07-23 22:28:06.835829

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '791a7f01d5b8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'users', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    # ### end Alembic commands ###
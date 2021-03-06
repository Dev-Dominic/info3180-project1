"""empty message

Revision ID: 9f35b1dfa2fd
Revises: 3042564a12d0
Create Date: 2020-04-10 21:04:50.683524

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f35b1dfa2fd'
down_revision = '3042564a12d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('profileImage', sa.String(length=150), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'profileImage')
    # ### end Alembic commands ###

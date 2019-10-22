"""add password_secure column

Revision ID: 0c36abda094e
Revises: e6d54318433e
Create Date: 2019-10-22 21:31:18.303728

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c36abda094e'
down_revision = 'e6d54318433e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_secure', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_secure')
    # ### end Alembic commands ###
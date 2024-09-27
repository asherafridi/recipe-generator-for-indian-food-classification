"""Remove profile_picture from User model

Revision ID: ca468b12b88b
Revises: 7222bb2c2f61
Create Date: 2024-09-10 20:46:46.698768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca468b12b88b'
down_revision = '7222bb2c2f61'
branch_labels = None
depends_on = None

def upgrade():
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('profile_picture')

def downgrade():
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('profile_picture', sa.String(length=150), nullable=True))
    # ### end Alembic commands ###

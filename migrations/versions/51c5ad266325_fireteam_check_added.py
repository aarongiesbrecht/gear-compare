"""fireteam check added

Revision ID: 51c5ad266325
Revises: 6420d571c5b0
Create Date: 2018-10-24 13:09:23.844749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51c5ad266325'
down_revision = '6420d571c5b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game_info', sa.Column('fireteam', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('game_info', 'fireteam')
    # ### end Alembic commands ###

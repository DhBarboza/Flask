"""empty message

Revision ID: 2fb8f45290bc
Revises: 
Create Date: 2021-05-25 12:55:05.212947

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2fb8f45290bc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('receitas',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('receita', sa.String(length=150), nullable=True),
    sa.Column('ingredientes', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('receitas')
    # ### end Alembic commands ###

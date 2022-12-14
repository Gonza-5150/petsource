"""empty message

Revision ID: 8ab38496e42f
Revises: fd7f641246fc
Create Date: 2022-11-02 00:51:45.033370

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ab38496e42f'
down_revision = 'fd7f641246fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agenda',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fecha', sa.Date(), nullable=False),
    sa.Column('hora', sa.Time(), nullable=False),
    sa.Column('retira', sa.Boolean(), nullable=False),
    sa.Column('direccion_retiro', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('hora')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('agenda')
    # ### end Alembic commands ###

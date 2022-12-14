"""empty message

Revision ID: cc96ffdf160c
Revises: cd5f73aeb94d
Create Date: 2022-11-02 16:26:04.305199

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc96ffdf160c'
down_revision = 'cd5f73aeb94d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('desparasitacion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.Column('fecha', sa.Date(), nullable=False),
    sa.Column('peso', sa.Integer(), nullable=False),
    sa.Column('tipo_desp', sa.String(length=120), nullable=False),
    sa.Column('mascota_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['mascota_id'], ['mascota.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('desparasitacion')
    # ### end Alembic commands ###

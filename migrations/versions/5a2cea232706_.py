"""empty message

Revision ID: 5a2cea232706
Revises: 979f09a03bee
Create Date: 2017-06-01 21:45:44.786763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a2cea232706'
down_revision = '979f09a03bee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('produto_id_unidade_medida_fkey', 'produto', type_='foreignkey')
    op.drop_column('produto', 'id_unidade_medida')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('produto', sa.Column('id_unidade_medida', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('produto_id_unidade_medida_fkey', 'produto', 'unidademedida', ['id_unidade_medida'], ['id_unidade_medida'])
    # ### end Alembic commands ###

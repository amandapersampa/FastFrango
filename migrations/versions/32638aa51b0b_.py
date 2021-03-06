"""empty message

Revision ID: 32638aa51b0b
Revises: 5a2cea232706
Create Date: 2017-06-01 22:01:40.023060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32638aa51b0b'
down_revision = '5a2cea232706'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('produto', sa.Column('id_unidade_medida', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'produto', 'unidademedida', ['id_unidade_medida'], ['id_unidade_medida'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'produto', type_='foreignkey')
    op.drop_column('produto', 'id_unidade_medida')
    # ### end Alembic commands ###

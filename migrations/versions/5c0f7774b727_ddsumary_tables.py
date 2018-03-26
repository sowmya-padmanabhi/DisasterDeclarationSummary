"""ddsumary tables

Revision ID: 5c0f7774b727
Revises: 
Create Date: 2018-03-25 19:21:47.319299

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c0f7774b727'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dd_summary',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('states', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_dd_summary_states'), 'dd_summary', ['states'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_dd_summary_states'), table_name='dd_summary')
    op.drop_table('dd_summary')
    # ### end Alembic commands ###

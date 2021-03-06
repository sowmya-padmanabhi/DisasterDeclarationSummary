"""ddsumaary tables

Revision ID: a5caae8f8d1e
Revises: 
Create Date: 2018-03-26 18:13:03.122682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5caae8f8d1e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dd_summary',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('disaster_number', sa.String(length=10), nullable=True),
    sa.Column('ih_program_declared', sa.String(length=10), nullable=True),
    sa.Column('ia_program_declared', sa.Integer(), nullable=True),
    sa.Column('pa_program_declared', sa.Integer(), nullable=True),
    sa.Column('hm_program_declared', sa.Integer(), nullable=True),
    sa.Column('states', sa.String(length=10), nullable=True),
    sa.Column('declaration_date', sa.DateTime(), nullable=True),
    sa.Column('fy_declared', sa.Integer(), nullable=True),
    sa.Column('disaster_type', sa.String(length=10), nullable=True),
    sa.Column('incident_type', sa.String(length=10), nullable=True),
    sa.Column('title', sa.String(length=10), nullable=True),
    sa.Column('incident_begin_date', sa.DateTime(), nullable=True),
    sa.Column('incident_end_date', sa.DateTime(), nullable=True),
    sa.Column('disaster_close_out_date', sa.DateTime(), nullable=True),
    sa.Column('declared_country_area', sa.String(length=10), nullable=True),
    sa.Column('place_code', sa.String(length=10), nullable=True),
    sa.Column('hash_', sa.Integer(), nullable=True),
    sa.Column('last_refresh', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_dd_summary_declaration_date'), 'dd_summary', ['declaration_date'], unique=False)
    op.create_index(op.f('ix_dd_summary_declared_country_area'), 'dd_summary', ['declared_country_area'], unique=False)
    op.create_index(op.f('ix_dd_summary_disaster_close_out_date'), 'dd_summary', ['disaster_close_out_date'], unique=False)
    op.create_index(op.f('ix_dd_summary_disaster_type'), 'dd_summary', ['disaster_type'], unique=False)
    op.create_index(op.f('ix_dd_summary_fy_declared'), 'dd_summary', ['fy_declared'], unique=False)
    op.create_index(op.f('ix_dd_summary_hash_'), 'dd_summary', ['hash_'], unique=False)
    op.create_index(op.f('ix_dd_summary_hm_program_declared'), 'dd_summary', ['hm_program_declared'], unique=False)
    op.create_index(op.f('ix_dd_summary_incident_begin_date'), 'dd_summary', ['incident_begin_date'], unique=False)
    op.create_index(op.f('ix_dd_summary_incident_end_date'), 'dd_summary', ['incident_end_date'], unique=False)
    op.create_index(op.f('ix_dd_summary_incident_type'), 'dd_summary', ['incident_type'], unique=False)
    op.create_index(op.f('ix_dd_summary_last_refresh'), 'dd_summary', ['last_refresh'], unique=False)
    op.create_index(op.f('ix_dd_summary_pa_program_declared'), 'dd_summary', ['pa_program_declared'], unique=False)
    op.create_index(op.f('ix_dd_summary_place_code'), 'dd_summary', ['place_code'], unique=False)
    op.create_index(op.f('ix_dd_summary_states'), 'dd_summary', ['states'], unique=False)
    op.create_index(op.f('ix_dd_summary_title'), 'dd_summary', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_dd_summary_title'), table_name='dd_summary')
    op.drop_index(op.f('ix_dd_summary_states'), table_name='dd_summary')
    op.drop_index(op.f('ix_dd_summary_place_code'), table_name='dd_summary')
    op.drop_index(op.f('ix_dd_summary_pa_program_declared'), table_name='dd_summary')
    op.drop_index(op.f('ix_dd_summary_last_refresh'), table_name='dd_summary')
    op.drop_index(op.f('ix_dd_summary_incident_type'), table_name='dd_summary')
    op.drop_index(op.f('ix_dd_summary_incident_end_date'), table_name='dd_summary')
    op.drop_index(op.f('ix_dd_summary_incident_begin_date'), table_name='dd_summary')
    op.drop_index(op.f('ix_dd_summary_hm_program_declared'), table_name='dd_summary')
    op.drop_index(op.f('ix_dd_summary_hash_'), table_name='dd_summary')
    op.drop_index(op.f('ix_dd_summary_fy_declared'), table_name='dd_summary')
    op.drop_index(op.f('ix_dd_summary_disaster_type'), table_name='dd_summary')
    op.drop_index(op.f('ix_dd_summary_disaster_close_out_date'), table_name='dd_summary')
    op.drop_index(op.f('ix_dd_summary_declared_country_area'), table_name='dd_summary')
    op.drop_index(op.f('ix_dd_summary_declaration_date'), table_name='dd_summary')
    op.drop_table('dd_summary')
    # ### end Alembic commands ###

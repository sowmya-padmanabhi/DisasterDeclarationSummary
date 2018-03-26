"""ddsummary table

Revision ID: 790fe6dfbffa
Revises: 446aeac2a500
Create Date: 2018-03-25 22:17:22.320205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '790fe6dfbffa'
down_revision = '446aeac2a500'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dd_summary', sa.Column('declaration_date', sa.DateTime(), nullable=True))
    op.add_column('dd_summary', sa.Column('declared_country_area', sa.String(length=10), nullable=True))
    op.add_column('dd_summary', sa.Column('disaster_close_out_date', sa.DateTime(), nullable=True))
    op.add_column('dd_summary', sa.Column('disaster_number', sa.String(length=10), nullable=True))
    op.add_column('dd_summary', sa.Column('disaster_type', sa.String(length=10), nullable=True))
    op.add_column('dd_summary', sa.Column('fy_declared', sa.Integer(), nullable=True))
    op.add_column('dd_summary', sa.Column('hash_', sa.Integer(), nullable=True))
    op.add_column('dd_summary', sa.Column('hm_program_declared', sa.Integer(), nullable=True))
    op.add_column('dd_summary', sa.Column('ia_program_declared', sa.Integer(), nullable=True))
    op.add_column('dd_summary', sa.Column('ih_program_declared', sa.String(length=10), nullable=True))
    op.add_column('dd_summary', sa.Column('incident_begin_date', sa.DateTime(), nullable=True))
    op.add_column('dd_summary', sa.Column('incident_end_date', sa.DateTime(), nullable=True))
    op.add_column('dd_summary', sa.Column('incident_type', sa.String(length=10), nullable=True))
    op.add_column('dd_summary', sa.Column('last_refresh', sa.String(length=20), nullable=True))
    op.add_column('dd_summary', sa.Column('pa_program_declared', sa.Integer(), nullable=True))
    op.add_column('dd_summary', sa.Column('place_code', sa.String(length=10), nullable=True))
    op.add_column('dd_summary', sa.Column('title', sa.String(length=10), nullable=True))
    op.create_index(op.f('ix_dd_summary_declaration_date'), 'dd_summary', ['declaration_date'], unique=False)
    op.create_index(op.f('ix_dd_summary_declared_country_area'), 'dd_summary', ['declared_country_area'], unique=False)
    op.create_index(op.f('ix_dd_summary_disaster_close_out_date'), 'dd_summary', ['disaster_close_out_date'], unique=False)
    op.create_index(op.f('ix_dd_summary_disaster_number'), 'dd_summary', ['disaster_number'], unique=False)
    op.create_index(op.f('ix_dd_summary_disaster_type'), 'dd_summary', ['disaster_type'], unique=False)
    op.create_index(op.f('ix_dd_summary_fy_declared'), 'dd_summary', ['fy_declared'], unique=False)
    op.create_index(op.f('ix_dd_summary_hash_'), 'dd_summary', ['hash_'], unique=False)
    op.create_index(op.f('ix_dd_summary_hm_program_declared'), 'dd_summary', ['hm_program_declared'], unique=False)
    op.create_index(op.f('ix_dd_summary_ia_program_declared'), 'dd_summary', ['ia_program_declared'], unique=False)
    op.create_index(op.f('ix_dd_summary_ih_program_declared'), 'dd_summary', ['ih_program_declared'], unique=False)
    op.create_index(op.f('ix_dd_summary_incident_begin_date'), 'dd_summary', ['incident_begin_date'], unique=False)
    op.create_index(op.f('ix_dd_summary_incident_end_date'), 'dd_summary', ['incident_end_date'], unique=False)
    op.create_index(op.f('ix_dd_summary_incident_type'), 'dd_summary', ['incident_type'], unique=False)
    op.create_index(op.f('ix_dd_summary_last_refresh'), 'dd_summary', ['last_refresh'], unique=False)
    op.create_index(op.f('ix_dd_summary_pa_program_declared'), 'dd_summary', ['pa_program_declared'], unique=False)
    op.create_index(op.f('ix_dd_summary_place_code'), 'dd_summary', ['place_code'], unique=False)
    op.create_index(op.f('ix_dd_summary_title'), 'dd_summary', ['title'], unique=False)
    op.drop_index('ix_dd_summary_iaProgramDeclared', table_name='dd_summary')
    op.drop_index('ix_dd_summary_ihprogramdeclared', table_name='dd_summary')
    op.drop_column('dd_summary', 'iaProgramDeclared')
    op.drop_column('dd_summary', 'ihprogramdeclared')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dd_summary', sa.Column('ihprogramdeclared', sa.VARCHAR(length=10), nullable=True))
    op.add_column('dd_summary', sa.Column('iaProgramDeclared', sa.INTEGER(), nullable=True))
    op.create_index('ix_dd_summary_ihprogramdeclared', 'dd_summary', ['ihprogramdeclared'], unique=False)
    op.create_index('ix_dd_summary_iaProgramDeclared', 'dd_summary', ['iaProgramDeclared'], unique=False)
    op.drop_index(op.f('ix_dd_summary_title'), table_name='dd_summary')
    op.drop_index(op.f('ix_dd_summary_place_code'), table_name='dd_summary')
    op.drop_index(op.f('ix_dd_summary_pa_program_declared'), table_name='dd_summary')
    op.drop_index(op.f('ix_dd_summary_last_refresh'), table_name='dd_summary')
    op.drop_index(op.f('ix_dd_summary_incident_type'), table_name='dd_summary')
    op.drop_index(op.f('ix_dd_summary_incident_end_date'), table_name='dd_summary')
    op.drop_index(op.f('ix_dd_summary_incident_begin_date'), table_name='dd_summary')
    op.drop_index(op.f('ix_dd_summary_ih_program_declared'), table_name='dd_summary')
    op.drop_index(op.f('ix_dd_summary_ia_program_declared'), table_name='dd_summary')
    op.drop_index(op.f('ix_dd_summary_hm_program_declared'), table_name='dd_summary')
    op.drop_index(op.f('ix_dd_summary_hash_'), table_name='dd_summary')
    op.drop_index(op.f('ix_dd_summary_fy_declared'), table_name='dd_summary')
    op.drop_index(op.f('ix_dd_summary_disaster_type'), table_name='dd_summary')
    op.drop_index(op.f('ix_dd_summary_disaster_number'), table_name='dd_summary')
    op.drop_index(op.f('ix_dd_summary_disaster_close_out_date'), table_name='dd_summary')
    op.drop_index(op.f('ix_dd_summary_declared_country_area'), table_name='dd_summary')
    op.drop_index(op.f('ix_dd_summary_declaration_date'), table_name='dd_summary')
    op.drop_column('dd_summary', 'title')
    op.drop_column('dd_summary', 'place_code')
    op.drop_column('dd_summary', 'pa_program_declared')
    op.drop_column('dd_summary', 'last_refresh')
    op.drop_column('dd_summary', 'incident_type')
    op.drop_column('dd_summary', 'incident_end_date')
    op.drop_column('dd_summary', 'incident_begin_date')
    op.drop_column('dd_summary', 'ih_program_declared')
    op.drop_column('dd_summary', 'ia_program_declared')
    op.drop_column('dd_summary', 'hm_program_declared')
    op.drop_column('dd_summary', 'hash_')
    op.drop_column('dd_summary', 'fy_declared')
    op.drop_column('dd_summary', 'disaster_type')
    op.drop_column('dd_summary', 'disaster_number')
    op.drop_column('dd_summary', 'disaster_close_out_date')
    op.drop_column('dd_summary', 'declared_country_area')
    op.drop_column('dd_summary', 'declaration_date')
    # ### end Alembic commands ###
"""empty message

Revision ID: 5754381d3a8f
Revises: 936f74a89f5f
Create Date: 2017-04-27 18:57:05.474910

"""

# revision identifiers, used by Alembic.
revision = '5754381d3a8f'
down_revision = '936f74a89f5f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('official',
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ss_id', sa.String(length=36), nullable=True),
    sa.Column('first_name', sa.String(length=32), nullable=True),
    sa.Column('last_name', sa.String(length=32), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('uniform_number', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_official_ss_id'), 'official', ['ss_id'], unique=True)
    op.create_table('venue',
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ss_id', sa.String(length=36), nullable=True),
    sa.Column('abbreviation', sa.String(length=64), nullable=True),
    sa.Column('capacity', sa.Integer(), nullable=True),
    sa.Column('city', sa.String(length=32), nullable=True),
    sa.Column('field_type', sa.String(length=16), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('slug', sa.String(length=32), nullable=True),
    sa.Column('state', sa.String(length=2), nullable=True),
    sa.Column('stadium_type', sa.String(length=32), nullable=True),
    sa.Column('time_zone', sa.String(length=32), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_venue_ss_id'), 'venue', ['ss_id'], unique=True)
    op.create_table('game',
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ss_id', sa.String(length=36), nullable=True),
    sa.Column('home_team_id', sa.Integer(), nullable=True),
    sa.Column('away_team_id', sa.Integer(), nullable=True),
    sa.Column('winning_team_id', sa.Integer(), nullable=True),
    sa.Column('venue_id', sa.Integer(), nullable=True),
    sa.Column('season', sa.Integer(), nullable=True),
    sa.Column('at_neutral_site', sa.Boolean(), nullable=True),
    sa.Column('attendance', sa.Integer(), nullable=True),
    sa.Column('away_team_outcome', sa.String(length=16), nullable=True),
    sa.Column('away_team_score', sa.Integer(), nullable=True),
    sa.Column('broadcast', sa.String(length=32), nullable=True),
    sa.Column('daytime', sa.Boolean(), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('ended_at', sa.DateTime(), nullable=True),
    sa.Column('home_team_outcome', sa.String(length=16), nullable=True),
    sa.Column('home_team_score', sa.Integer(), nullable=True),
    sa.Column('humidity', sa.String(length=32), nullable=True),
    sa.Column('interval', sa.String(length=32), nullable=True),
    sa.Column('interval_number', sa.Integer(), nullable=True),
    sa.Column('interval_type', sa.String(length=32), nullable=True),
    sa.Column('label', sa.String(length=64), nullable=True),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('on', sa.String(length=64), nullable=True),
    sa.Column('period', sa.Integer(), nullable=True),
    sa.Column('period_label', sa.String(length=16), nullable=True),
    sa.Column('score', sa.String(length=16), nullable=True),
    sa.Column('score_differential', sa.Integer(), nullable=True),
    sa.Column('scoreline', sa.String(length=64), nullable=True),
    sa.Column('slug', sa.String(length=64), nullable=True),
    sa.Column('started_at', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(length=16), nullable=True),
    sa.Column('internet_coverage', sa.String(length=32), nullable=True),
    sa.Column('satellite_coverage', sa.String(length=32), nullable=True),
    sa.Column('television_coverage', sa.String(length=32), nullable=True),
    sa.Column('temperature', sa.String(length=8), nullable=True),
    sa.Column('temperature_unit', sa.String(length=8), nullable=True),
    sa.Column('timestamp', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('weather_conditions', sa.String(length=64), nullable=True),
    sa.Column('wind_direction', sa.String(length=32), nullable=True),
    sa.Column('wind_speed', sa.Integer(), nullable=True),
    sa.Column('wind_speed_unit', sa.String(length=8), nullable=True),
    sa.ForeignKeyConstraint(['away_team_id'], ['team.id'], ),
    sa.ForeignKeyConstraint(['home_team_id'], ['team.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venue.id'], ),
    sa.ForeignKeyConstraint(['winning_team_id'], ['team.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_game_ss_id'), 'game', ['ss_id'], unique=True)
    op.alter_column(u'team', 'latitude',
               existing_type=sa.NUMERIC(precision=8, scale=0),
               nullable=False)
    op.alter_column(u'team', 'longitude',
               existing_type=sa.NUMERIC(precision=8, scale=0),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(u'team', 'longitude',
               existing_type=sa.NUMERIC(precision=8, scale=0),
               nullable=True)
    op.alter_column(u'team', 'latitude',
               existing_type=sa.NUMERIC(precision=8, scale=0),
               nullable=True)
    op.drop_index(op.f('ix_game_ss_id'), table_name='game')
    op.drop_table('game')
    op.drop_index(op.f('ix_venue_ss_id'), table_name='venue')
    op.drop_table('venue')
    op.drop_index(op.f('ix_official_ss_id'), table_name='official')
    op.drop_table('official')
    # ### end Alembic commands ###

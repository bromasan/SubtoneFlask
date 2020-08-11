"""adding artists

Revision ID: 15d63469e93a
Revises: 96ece1634c1f
Create Date: 2020-08-10 18:54:00.290555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15d63469e93a'
down_revision = '96ece1634c1f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('big_artist',
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('genre1', sa.String(length=64), nullable=True),
    sa.Column('genre2', sa.String(length=64), nullable=True),
    sa.Column('genre3', sa.String(length=64), nullable=True),
    sa.Column('danceability', sa.Numeric(precision=10, scale=7), nullable=True),
    sa.Column('energy', sa.Numeric(precision=10, scale=7), nullable=True),
    sa.Column('key', sa.Numeric(precision=10, scale=7), nullable=True),
    sa.Column('loudness', sa.Numeric(precision=10, scale=7), nullable=True),
    sa.Column('mode', sa.Numeric(precision=10, scale=7), nullable=True),
    sa.Column('speechiness', sa.Numeric(precision=10, scale=7), nullable=True),
    sa.Column('acousticness', sa.Numeric(precision=10, scale=7), nullable=True),
    sa.Column('instrumentalness', sa.Numeric(precision=10, scale=7), nullable=True),
    sa.Column('liveness', sa.Numeric(precision=10, scale=7), nullable=True),
    sa.Column('valence', sa.Numeric(precision=10, scale=7), nullable=True),
    sa.Column('tempo', sa.Numeric(precision=10, scale=7), nullable=True),
    sa.PrimaryKeyConstraint('name')
    )
    op.create_table('small_artist',
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('genre1', sa.String(length=64), nullable=True),
    sa.Column('genre2', sa.String(length=64), nullable=True),
    sa.Column('genre3', sa.String(length=64), nullable=True),
    sa.Column('danceability', sa.Numeric(precision=10, scale=7), nullable=True),
    sa.Column('energy', sa.Numeric(precision=10, scale=7), nullable=True),
    sa.Column('key', sa.Numeric(precision=10, scale=7), nullable=True),
    sa.Column('loudness', sa.Numeric(precision=10, scale=7), nullable=True),
    sa.Column('mode', sa.Numeric(precision=10, scale=7), nullable=True),
    sa.Column('speechiness', sa.Numeric(precision=10, scale=7), nullable=True),
    sa.Column('acousticness', sa.Numeric(precision=10, scale=7), nullable=True),
    sa.Column('instrumentalness', sa.Numeric(precision=10, scale=7), nullable=True),
    sa.Column('liveness', sa.Numeric(precision=10, scale=7), nullable=True),
    sa.Column('valence', sa.Numeric(precision=10, scale=7), nullable=True),
    sa.Column('tempo', sa.Numeric(precision=10, scale=7), nullable=True),
    sa.PrimaryKeyConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('small_artist')
    op.drop_table('big_artist')
    # ### end Alembic commands ###
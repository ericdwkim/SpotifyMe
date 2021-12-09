"""empty message

Revision ID: 5d8d5ffff5f3
Revises: a9ae3929bbf7
Create Date: 2021-12-09 12:52:05.061003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d8d5ffff5f3'
down_revision = 'a9ae3929bbf7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accounts',
    sa.Column('account_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('user_email', sa.String(length=255), nullable=False),
    sa.Column('user_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('account_id'),
    sa.UniqueConstraint('user_email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('albums',
    sa.Column('album_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('album_title', sa.String(length=128), nullable=False),
    sa.Column('album_length', sa.Integer(), nullable=False),
    sa.Column('artwork_url', sa.String(length=280), nullable=False),
    sa.Column('num_of_songs', sa.Integer(), nullable=False),
    sa.Column('release_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('album_id')
    )
    op.create_table('artists',
    sa.Column('artist_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('artist_name', sa.String(length=128), nullable=False),
    sa.Column('artist_bio', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('artist_id')
    )
    op.create_table('audios',
    sa.Column('audio_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('audio_url', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('audio_id')
    )
    op.create_table('groups',
    sa.Column('group_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('group_name', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('group_id')
    )
    op.create_table('songs',
    sa.Column('song_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('song_title', sa.String(length=128), nullable=False),
    sa.Column('song_writer', sa.String(length=128), nullable=False),
    sa.Column('song_producer', sa.String(length=128), nullable=False),
    sa.Column('song_length', sa.Integer(), nullable=False),
    sa.Column('release_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('song_id')
    )
    op.create_table('accounts_artists',
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['accounts.account_id'], ),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.artist_id'], ),
    sa.PrimaryKeyConstraint('account_id', 'artist_id')
    )
    op.create_table('albums_artists',
    sa.Column('album_id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['album_id'], ['albums.album_id'], ),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.artist_id'], ),
    sa.PrimaryKeyConstraint('album_id', 'artist_id')
    )
    op.create_table('groups_artists',
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.artist_id'], ),
    sa.ForeignKeyConstraint(['group_id'], ['groups.group_id'], ),
    sa.PrimaryKeyConstraint('group_id', 'artist_id')
    )
    op.create_table('songs_albums',
    sa.Column('song_id', sa.Integer(), nullable=False),
    sa.Column('album_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['album_id'], ['albums.album_id'], ),
    sa.ForeignKeyConstraint(['song_id'], ['songs.song_id'], ),
    sa.PrimaryKeyConstraint('song_id', 'album_id')
    )
    op.create_table('songs_artists',
    sa.Column('song_id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.artist_id'], ),
    sa.ForeignKeyConstraint(['song_id'], ['songs.song_id'], ),
    sa.PrimaryKeyConstraint('song_id', 'artist_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('songs_artists')
    op.drop_table('songs_albums')
    op.drop_table('groups_artists')
    op.drop_table('albums_artists')
    op.drop_table('accounts_artists')
    op.drop_table('songs')
    op.drop_table('groups')
    op.drop_table('audios')
    op.drop_table('artists')
    op.drop_table('albums')
    op.drop_table('accounts')
    # ### end Alembic commands ###

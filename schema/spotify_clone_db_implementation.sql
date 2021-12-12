CREATE TABLE songs (
    song_id SERIAL,
    song_title TEXT NOT NULL,
    song_writer TEXT NOT NULL,
    song_producer TEXT NOT NULL,
    song_length INT NOT NULL,
    release_date DATE NOT NULL,
    PRIMARY KEY (song_id)
);

CREATE TABLE albums (
    album_id SERIAL,
    album_title TEXT NOT NULL,
    album_length FLOAT NOT NULL,
    artwork_url TEXT NOT NULL,
    num_of_songs INT NOT NULL,
    release_date DATE NOT NULL,
    PRIMARY KEY (album_id)
);

CREATE TABLE groups (
    group_id SERIAL,
    group_name TEXT NOT NULL,
    PRIMARY KEY (group_id)
);

CREATE TABLE accounts (
    account_id SERIAL,
    username TEXT NOT NULL UNIQUE,
    user_email TEXT NOT NULL UNIQUE,
    user_password TEXT NOT NULL,
    PRIMARY KEY (account_id)
);

CREATE TABLE artists (
    artist_id SERIAL,
    artist_name TEXT NOT NULL,
    artist_bio TEXT,
    PRIMARY KEY (artist_id)
);

-- many-to-many bridge tables below

CREATE TABLE songs_artists (
    song_id INT NOT NULL,
    artist_id INT NOT NULL,
    PRIMARY KEY (song_id, artist_id)
);

CREATE TABLE albums_artists (
    album_id INT NOT NULL,
    artist_id INT NOT NULL,
    PRIMARY KEY (album_id, artist_id)
);

CREATE TABLE groups_artists (
    group_id INT NOT NULL,
    artist_id INT NOT NULL,
    PRIMARY KEY (group_id, artist_id)
);
-- =================== fk constraints below ================================

-- enforces many-to-one relation for songs&albums
ALTER TABLE public.songs
ADD COLUMN album_id INT UNIQUE;

ALTER TABLE songs
ADD CONSTRAINT fk_songs_albums
FOREIGN KEY (album_id)
REFERENCES albums;

-- enforces many-to-many relation for songs&artists
ALTER TABLE songs_artists
ADD CONSTRAINT fk_songs_artists_songs
FOREIGN KEY (song_id)
REFERENCES songs;

ALTER TABLE songs_artists
ADD CONSTRAINT fk_songs_artists_artists
FOREIGN KEY (artist_id)
REFERENCES artists;

-- enforces many-to-many relation for albums&artists
ALTER TABLE albums_artists
ADD CONSTRAINT fk_albums_artists_albums
FOREIGN KEY (album_id)
REFERENCES albums;

ALTER TABLE albums_artists
ADD CONSTRAINT fk_albums_artists_artists
FOREIGN KEY (artist_id)
REFERENCES artists;

-- enforces many-to-many relation for groups&artists
ALTER TABLE groups_artists
ADD CONSTRAINT fk_groups_artists_groups
FOREIGN KEY (group_id)
REFERENCES groups;

ALTER TABLE groups_artists
ADD CONSTRAINT fk_groups_artists_artists
FOREIGN KEY (artist_id)
REFERENCES artists;

-- enforces one-to-one relation for accounts&artists
ALTER TABLE public.accounts
ADD COLUMN artist_id INT UNIQUE;

ALTER TABLE accounts
ADD CONSTRAINT fk_accounts_artists
FOREIGN KEY (artist_id)
REFERENCES artists;
from ...flask.spotify.src.models import Song, Album, Group, Account, Artist

def test_new_song():
    """
    GIVEN a Song model
    WHEN a new Song is created
    THEN check the title, writer, producer, length, and release_date fields are defined correctly
    """
    song = Song(
        'Stan', 
        'Eminem',
        'Dr. Dre',
        6.44,
        '05-23-2000'
    )

    assert song.song_title == 'Stan'
    assert song.song_writer == 'Eminem'
    assert song.song_producer == 'Dr. Dre'
    assert song.song_length == 6.44
    assert song.release_date == '05-23-2000'

def test_new_album():
    """
    TODO: implement 
    """

def test_new_group():
    """
    TODO: implement 
    """

def test_new_account():
    """
    TODO: implement 
    """

def test_new_artist():
    """
    TODO: implement 
    """

"""
@dev: https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/
https://pytest-flask.readthedocs.io/en/latest/

"""
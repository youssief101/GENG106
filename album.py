def make_album(artist_name, album_title, songs_count=None):
    """builds a dictionary describing a music album"""
    album_info = {
        'artist name': artist_name.title(), 
        'album name': album_title.title()
    }

    if songs_count:
        album_info['songs counter'] = songs_count

    return album_info

# with number of songs
album_data = make_album('bablo', 'the avagalance', 30)
print(album_data)

# without number of songs
album_data = make_album('bablo', 'the avagalance')
print(album_data)
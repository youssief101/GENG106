def make_album(artist_name, album_title, songs_count=None):
    """builds a dictionary describing a music album"""
    album_info = {
        'artist name': artist_name.title(), 
        'album name': album_title.title()
    }

    if songs_count:
        album_info['songs counter'] = songs_count

    return album_info

while True:
    """Get the album data"""
    print(f"press q to quit at anytime.")

    # get the album data
    artist = input('artist name: ')
    if artist == 'q':
        break
    album = input('album name: ')
    if album == 'q':
        break
    songs_count = input('number of songs: ')
    if songs_count == 'q':
        break

    # show the ablum data
    album_data = make_album(artist, album, songs_count)
    print(album_data)
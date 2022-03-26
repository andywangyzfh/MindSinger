from os import spawnl
import spotipy
import sys
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

'''
Parameter: 
 - q: the string we want to search (e.g. 'sad')
'''
def search(newq): 
    q = str() 
    q = str(newq)

    auth_manager = SpotifyClientCredentials(client_id= 'c0852b805bac480aa7ae57f125629e7a', \
        client_secret= '156ea9da4b0245aebe02b7c84da0826a')
    # scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager=auth_manager)

    results = sp.search(q='playlist:' + q, type='playlist')
    items = results['playlists']['items']

    for i in range(len(items)): 
        playlist = items[i]

        # If the playlist name contains the following word, just ignore it 
        # blacklist = ['workout', 'gym']

        if ('workout' not in playlist['name']):
            print(playlist['name'], playlist['images'][0]['url']) 


# search('sad')
# search('happy')


        

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

def search(newq): 
    '''
    Parameter
    - q: the string we want to search (e.g. 'sad')
    Return 
    - tuple type, (<name of the playlist>, <image url>)
    '''
    q = str(newq)

    auth_manager = SpotifyClientCredentials(client_id='c0852b805bac480aa7ae57f125629e7a',
                                            client_secret='156ea9da4b0245aebe02b7c84da0826a')
    # scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager=auth_manager)

    results = sp.search(q='playlist:' + q, type='playlist')
    items = results['playlists']['items']

    blacklist = ['workout', 'gym'] 

    ifContainBlackword = False

    for i in range(len(items)): 
        playlist = items[i]
        name = playlist['name'] 
        
        for blackword in blacklist: 
            # if the name contains blackword, just skip to the next playlist 
            if (blackword in name ):
                ifContainBlackword = True 
                break
        if (ifContainBlackword == False):
            return ( (playlist['name']), playlist['images'][0]['url'] )
            # if managed to print out one -> terminate 
            break 

res = search('sad')
print(res)
# search('happy')

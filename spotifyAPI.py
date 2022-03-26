from ast import Try
from http import client
from logging import exception
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials


SPOTIPY_CLIENT_ID = 'c0852b805bac480aa7ae57f125629e7a'
SPOTIPY_CLIENT_SECRET = '156ea9da4b0245aebe02b7c84da0826a'
# SPOTIPY_CLIENT_SECRET = 'BQC2QReF0tK6_PFij8pOJlt5X1zTRxaT8oGSG-h11-CaeJ4o3h2vydH8cU-KYKZHQDR4AxwE_F_SB2oAUG_7jyB4CX1iC4IfwbA-omXCts7dspgTo58xw7Q6SKTIF6whBupSO4Iz6LvmajCbkKenTNMTPAJ7Ahi6z9Q103U'
# SPOTIPY_REDIRECT_URI = 'http://127.0.0.1:5000/'
SPOTIPY_REDIRECT_URI = 'http://example.com/callback/'
SCOPE = "user-read-playback-state,user-modify-playback-state"

def connect(): 
    auth_manager = SpotifyOAuth(client_id = SPOTIPY_CLIENT_ID, client_secret= SPOTIPY_CLIENT_SECRET, redirect_uri = SPOTIPY_REDIRECT_URI, scope = SCOPE)

    clientCredentials = SpotifyClientCredentials(client_id='c0852b805bac480aa7ae57f125629e7a',
                                        client_secret='156ea9da4b0245aebe02b7c84da0826a')
    sp = spotipy.Spotify(auth_manager=auth_manager, client_credentials_manager= clientCredentials )
    return sp 

def search(newq): 
    '''
    Parameter
    - q: the string we want to search (e.g. 'sad')
    Return 
    - tuple type, (<name of the playlist>, <image url>, <playlist uri>)
    '''
    q = str(newq)

    sp = connect()
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
        # if the name does not contain blacklist words 
        if (ifContainBlackword == False): 
            return ( (playlist['name']), playlist['images'][0]['url'], playlist['uri'], sp )
# res = search('sad')
# print(res)
# res = search('happy')
# print(res)

def play(uri): 
    sp = connect() 
    # Change track
    sp.start_playback(context_uri=str(uri))
    return 

def pause(): 
    sp = connect() 
    # if Spotify is not playing anything, then pause action will cause error 
    try:
        sp.pause_playback()
    except Exception:
        pass
    return 

# pause()
# resUri = search('happy')[2]
# print(resUri)
# play(resUri )
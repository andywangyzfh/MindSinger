from flask import Flask, request, render_template
from spotifyAPI import search, play, pause
import spotipy

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    text = request.form['input-text']
    name, img, uri, sp = search(text) 
    uriCompact = uri
    uriCompact = uri.replace("spotify:playlist:", "")

    spotifyEmbed = '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/' + uriCompact + '?utm_source=generator" width="100%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>' 

    # autoplay = '''
    # <script src="./javascript/jquery.js"></script>
    # '''

    pause()
    # play(uri)

    return 'The texts you input appears: {}'.format(text) + spotifyEmbed 
    # return 'The texts you input appears: {}'.format(text) + spotifyEmbed


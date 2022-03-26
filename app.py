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
    # search(text)
    # return 'You entered: {}'.format(text)
    return render_template('playsong.html')

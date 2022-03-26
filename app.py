from flask import Flask, request, render_template
from spotifyAPI import search

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    text = request.form['input-text']
    # name, img, uri = str(search(text) )
    # uri.replace("spotify:playlist:", "")

    # spotifyEmbed = '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/"' \
    #     + uri + '"?utm_source=generator" width="100%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>' 

    return 'The texts you input appears: {}'.format(text)
    # return 'The texts you input appears: {}'.format(text) + spotifyEmbed


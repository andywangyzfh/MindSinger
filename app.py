from flask import Flask, request, render_template
from spotifyAPI import search

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    text = request.form['input-text']
    search(text)
    return 'You entered: {}'.format(text)

# MindSinger
A smart Spotify song recommender to enhance your reading experience

Demo can be found [here](https://devpost.com/software/mindsinger).

## Usage
Install prerequisites: execute `pip3 install --user nlpk flask spotipy scikit-learn`.  
Go to the root level and execute `flask run`.

## Inspiration

We all like to listen to some music when reading articles online. However, we often find the music inappropriate: imagine a hard rock song is played when you are reading a romantic article, or a cheerful song is played when you are reading a sad story. Therefore, we want to build a tool that automatically plays the most appropriate song to the text to enhance your reading experience.

## What it does

MindSinger takes a text input and conduct sentiment analysis on it. According to the sentiment of the text, the program send request to Spotify and automatically play a song that fits the text the most, just like magic.

## How we built it

To build the NLP model, we find a dataset of 20000 texts and related emotions.  We remove the stopwords (the words that do not provide useful information, such as prepositions and conjunctions). We "stem" a text, that is, reduce the words to their stem. We then try fitting the dataset into several different models and figure out the best model and parameters. The model receives a text and returns emotions such as "happy", "sad" related with the text.
To build the front-end, we use a Python library Flask. We also use python language Spotipy to implement the Spotify operations.

## Challenges we ran into

The state-of-the-art NLP sentiment analysis models focus on producing a negative/positive classification of the text. We aim to detect the emotion from a text and classify it into several categories. So instead of using an existing model, we build our own. We first do some feature engineering on a dataset. For example, we "stem" a text, that is, reduce the words to their stem. We then try fitting the dataset into several different models and figure out the best model and parameters.
We also met some challenges in the software development process. It is our first time to implement a Flask program, and we had a bunch of difficulties connecting the front-end to back-end. Luckily, we fixed all of them. 

## Accomplishments that we're proud of

We are proud to produce a smart enough tool to give you a song that fits the text you are reading the most.

## What we learned

None of our team members have written NLP models before. We learned about techniques to preprocess text to feed into NLP model. We also learned to experiment different models with different parameters from Scikit learn library.  We also learned to make front-end webpage work with back-end NLP model

## What's next for MindSinger

Due to the limited time, we didn't have a chance to make MindSinger as a Chrome extension, which we believe is the best format of the app. For the next steps, we will implement MindSinger as a browser extension. 
Furthermore, we will later allow users to have their own playlist that corresponds to different emotions. 
Of course, our text sentiment analysis model is far from perfect. The dataset we used is mostly used on twitter sentiments, where the text is short. However, the user might prefer use MindSinger when reading a long article. Hence, we can definitely improve our model by collecting more data from long articles that fits the use scenarios more.

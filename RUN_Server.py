#!/usr/bin/env python
# coding: UTF-8

import os
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def list_movies():
    movies_list = []
    for dirpath, dirnames, filenames in os.walk("./static/movie"):
            for filename in filenames:
                if os.path.splitext(filename)[-1] == ".mp4":
                    filename_utf8 = unicode(filename, 'utf8')
                    movies_list.append(filename_utf8)
    return render_template('homepage.html', movies_list=movies_list)


@app.route('/player/<movie_name>')
def play_movie(movie_name):
    return render_template('player.html', movie_name=movie_name)

if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0')

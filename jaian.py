from flask import Flask
import os
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/janken/')
def janken():
    r = np.random.random()
    if r < 1/3:
        return 'ぐう'
    elif r < 2/3:
        return 'ちょき〜ん'
    else:
        return 'ぱぁ'


@app.route('/user/')
def user():
    #return os.environ['USER']
    return os.environ['HOME']


if __name__ == '__main__':
    app.run()
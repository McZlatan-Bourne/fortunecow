#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, I'm Cow, and i will be giving you fortunes"

if __name__ == '__main__':
    app.run(debug=True)
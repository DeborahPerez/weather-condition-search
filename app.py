#!/usr/bin/env python
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Weather condition search is a work in progress..."

if __name__ == "__main__":
    app.run()

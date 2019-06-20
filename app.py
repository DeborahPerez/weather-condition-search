#!/usr/bin/env python
import os
from flask import Flask


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

@app.route('/')
def hello():
    return "Weather condition search is a work in progress..."

if __name__ == "__main__":
    app.run()

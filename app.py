#!/usr/bin/env python
import os
from flask import Flask, render_template, request
import weather_api
from condition_types import conditions
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
print (os.environ['APP_SETTINGS'])

@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = []
    if request.method == "POST":
        # get weather condition that the person has entered
        try:
            condition = request.form['condition']
            if condition.lower() in conditions:
                results = weather_api.get_cities_for_condition(condition)
            else:
                errors.append("Not an acceptable weather condition")
                return render_template('index.html', errors=errors)

        except:
            errors.append("Unable to get condition. Please try again!")
            return render_template('index.html', errors=errors)

    return render_template('index.html', errors=errors, results=results)

if __name__ == "__main__":
    app.run()

#!/usr/bin/env python3
""" A module that defines a flask app """
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """It returns the index.html template"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)

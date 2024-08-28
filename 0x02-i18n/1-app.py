#!/usr/bin/env python3
""" A module that defines a flask app """
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ A Flask Babel configuration class"""
    LANGUAGES = ['en', 'fr']
    Babel.default_locale = 'en'
    Babel.default_timezone = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
@app.route('/', strict_slashes=False)
def index():
    """It returns the index.html template"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()

#!/usr/bin/env python3
""" A module that defines a flask app """
from typing import Dict, Union
from flask import Flask, render_template, request, g
from flask_babel import Babel, _


class Config:
    """ A Flask Babel configuration class"""
    LANGUAGES = ['en', 'fr']
    Babel.default_locale = 'en'
    Babel.default_timezone = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """It returns the user dictionary"""
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request():
    """It sets the user as a global"""
    g.user = get_user()
    print(f'Current User: {g.user}')


@babel.localeselector
def get_locale():
    """It returns the best match with the supported languages"""
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """It returns the index.html template"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)

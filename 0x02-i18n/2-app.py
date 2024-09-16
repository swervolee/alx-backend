#!/usr/bin/env python3
"""
A FLASK APP
"""

from flask import Flask, g, request, render_template
from flask_babel import Babel, gettext, ngettext, format_datetime
from datetime import datetime
from typing import Any

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=["GET"], strict_slashes=False)
def index() -> Any:
    """
    Index page
    """
    return render_template("0-index.html")


if __name__ == '__main__':
    app.run(debug=True)

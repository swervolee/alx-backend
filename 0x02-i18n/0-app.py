#!/usr/bin/env python3
"""
A FLASK APP
"""
from flask import Flask, g, request, render_template
from flask_babel import Babel, gettext, ngettext, format_datetime
from datetime import datetime


app = Flask(__name__)


@app.route('/', methods=["GET"], strict_slashes=False)
def index() -> Any:
    """
    Index page
    """
    return render_template("0-index.html")

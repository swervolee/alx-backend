#!/usr/bin/env python3
"""
A FLASK APP
"""
from flask import Flask, g, request, render_template
from flask_babel import Babel, gettext, ngettext, format_datetime
from datetime import datetime


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Homepage():
    """
    HOMEPAGE
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

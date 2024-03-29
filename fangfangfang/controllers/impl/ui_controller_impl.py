import flask
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
__favicon_location__ = os.path.join(__location__, 'static/favicon.ico')
__index_location__ = os.path.join(__location__, 'static/index.html')
__logo_location__ = os.path.join(__location__, 'static/logo.png')

def favicon():
    return flask.send_file(__favicon_location__)


def index():
    return flask.send_file(__index_location__)


def logo():
    return flask.send_file(__logo_location__)

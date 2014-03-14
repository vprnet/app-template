#!/usr/local/bin/python2.7

from flask import Flask
import sys
from flask_frozen import Freezer
from upload_s3 import set_metadata
from config import AWS_DIRECTORY

app = Flask(__name__)
app.config.from_object('config')

from views import *

# Serving from s3 leads to some complications in how static files are served
if len(sys.argv) > 1 and sys.argv[1] == 'build':
    PROJECT_ROOT = '/' + AWS_DIRECTORY
else:
    PROJECT_ROOT = '/'


class WebFactionMiddleware(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        environ['SCRIPT_NAME'] = PROJECT_ROOT
        return self.app(environ, start_response)

app.wsgi_app = WebFactionMiddleware(app.wsgi_app)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer = Freezer(app)
        freezer.freeze()
        set_metadata()
    else:
        app.run(debug=True)

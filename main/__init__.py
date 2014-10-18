from flask import Flask
from config import WEBFACTION_PATH

app = Flask(__name__)
app.config.from_object('main.config')

from main import views


class WebFactionMiddleware(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        environ['SCRIPT_NAME'] = WEBFACTION_PATH
        return self.app(environ, start_response)


if __name__ == '__main__':
    app.wsgi_app = WebFactionMiddleware(app.wsgi_app)
    app.run()

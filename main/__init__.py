from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from main import views


class WebFactionMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        environ['SCRIPT_NAME'] = '/template'
        return self.app(environ, start_response)

app.wsgi_app = WebFactionMiddleware(app.wsgi_app)

if __name__ == '__main__':
    app.run()

from flask import Flask

db = 'database'

# flask run -> create_app()
def create_app():
    print('run: create_app()')
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello World'

    return app

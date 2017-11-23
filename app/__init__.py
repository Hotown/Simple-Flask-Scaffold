from flask import Flask


def create_app(config_file):
    app = Flask(__name__)
    app.config.from_object(config_file)

    # init flask-sqlalchemy
    from app.basemodel import db
    db.init_app(app)

    @app.route('/')
    def api_root():
        return 'Welcome to simple flask scaffold!'

    from app.controller import user
    app.register_blueprint(user, url_prefix='/user')

    return app

from flask_mail import Message
from flask_mail import Mail
from flask import Flask
from app.utils.utils import require
from app.controller import user

def create_app(config_file):
    app = Flask(__name__)
    app.config.from_object(config_file)
    mail = Mail(app)

    # init flask-sqlalchemy
    from app.basemodel import db
    db.init_app(app)


    @app.route('/')
    def api_root():
        return 'Welcome to simple flask scaffold!'


    app.register_blueprint(user, url_prefix='/user')



    @app.route("/mail")
    def index():

        msg = Message("Hello",
                      recipients=["your@mail.com"])
        mail.send(msg)


    @app.route("/validate",methods=(["POST"]))
    @require('param1','param2')
    def validate():
        return 'hello'

    return app

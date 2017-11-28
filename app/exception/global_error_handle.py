from flask import Flask, Blueprint, Response
from flask.ext.errorhandler import ErrorHandler
import json

app = Flask(__name__)
api_blueprint = Blueprint('api', 'api')
web_blueprint = Blueprint('web', 'web')

errorhandler = ErrorHandler()
errorhandler.init_app(app)


@errorhandler.errorhandler(api_blueprint)
def handle_error(e):

    data = {
        'code': e['code'],
        'message': e['data']
    }
    response = Response(json.dumps(data),
                        mimetype='application/json',
                        status=202)
    return response

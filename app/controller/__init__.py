from flask import Blueprint

user = Blueprint('user', __name__)

from app.controller import user_controller

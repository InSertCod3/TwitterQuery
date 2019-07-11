from flask import Blueprint

BP_API = Blueprint('api', __name__)

from . import users, general
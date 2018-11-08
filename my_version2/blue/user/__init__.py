from flask import Blueprint

user = Blueprint('user', __name__)

# from . import user_info
from user_info import *

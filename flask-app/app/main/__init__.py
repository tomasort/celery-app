from flask import Blueprint

main = Blueprint('main', __name__, static_folder='static', template_folder='templates')
from app.main import views, tasks
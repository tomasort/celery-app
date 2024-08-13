from flask import current_app, render_template
from flask_login import login_required
from app.main import main
from app import db

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/secret')
@login_required
def secret():
    return render_template('secret.html')


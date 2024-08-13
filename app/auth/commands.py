from flask import current_app
from app import db
import click
from app.auth.models import User
from app.auth import auth

@auth.cli.command('create')
@click.argument("name")
@click.argument('email')
@click.argument('password')
def create_user(name, email, password):
    user = User(username=name, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    current_app.logger.info("created a new User in the cli {name}, ")
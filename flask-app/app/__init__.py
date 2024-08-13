import os
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from logging.handlers import RotatingFileHandler
from celery import Celery, Task
from app.config import config
import logging
from flask_login import LoginManager
from flask_socketio import SocketIO


# instantiate the extensions
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
socketio = SocketIO()

def create_app(config_name=None) -> Flask:
    if config_name is None:
        config_name = os.environ.get("FLASK_CONFIG", "development")

    # instantiate the app
    app = Flask(__name__)

    # set config
    app.config.from_object(config[config_name])

    # set up extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    socketio.init_app(app)

    # set up Celery
    celery_init_app(app)

    # register error handlers
    register_error_handlers

    # register blueprints
    from app.main import main 
    app.register_blueprint(main)

    from app.auth import auth 
    app.register_blueprint(auth, cli_group='auth')
    login.login_view = "auth.login"

    # set up logging
    setup_logging(app)  

    return app

def setup_logging(app) -> None:
    if not os.path.exists(f'{__name__}/logs'):  
        os.mkdir(f'{__name__}/logs')
    file_handler = RotatingFileHandler(f'{__name__}/logs/{__name__}.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.info('app startup')


def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=FlaskTask)
    celery_app.config_from_object(app.config["CELERY"])
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app

def register_error_handlers(app):

    # 400 - Bad Request
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('400.html'), 400

    # 403 - Forbidden
    @app.errorhandler(403)
    def forbidden(e):
        return render_template('403.html'), 403

    # 404 - Page Not Found
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    # 405 - Method Not Allowed
    @app.errorhandler(405)
    def method_not_allowed(e):
        return render_template('405.html'), 405

    # 500 - Internal Server Error
    @app.errorhandler(500)
    def server_error(e):
        return render_template('500.html'), 500
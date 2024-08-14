import os
from pathlib import Path


class BaseConfig:
    """Base configuration"""
    BASE_DIR = Path(__file__).parent.parent

    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', f'sqlite:///{BASE_DIR}/db.sqlite3')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'f64ac936a2d9b7370c6b55b727f92c18') # use secrets.token_hex(32) or something like that to generate a key
    CELERY=dict(
        broker_url=os.environ.get("BROKER_URL", "redis://127.0.0.1:6379/0"),
        result_backend=os.environ.get("RESULT_BACKEND", "redis://127.0.0.1:6379/0"),
    )

class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG = True


class ProductionConfig(BaseConfig):
    """Production configuration"""
    DEBUG = False


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}

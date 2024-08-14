import click
from app import create_app, socketio

app = create_app()
celery_app = app.extensions["celery"]

@click.command()
@click.option('-h', '--host', default='0.0.0.0', help='The hostname to listen on.')
@click.option('-p', '--port', default=5000, help='The port of the web server.')
@click.option('-d', '--debug', is_flag=True, help='Enable debug mode.')
def run_app(host, port, debug):
    """Run the Flask-SocketIO application with the given configuration."""
    socketio.run(app, host=host, port=port, debug=debug, use_reloader=debug)

if __name__ == '__main__':
    run_app()
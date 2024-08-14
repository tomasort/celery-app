import os
import time
from celery import shared_task
from flask_socketio import SocketIO

@shared_task(ignore_result=False)
def add_together(a: int, b: int) -> int:
    return a + b

@shared_task(ignore_result=False)
def test_task() -> None:
    socketio = SocketIO(message_queue=os.environ.get("BROKER_URL", 'redis://localhost:6379/0'))
    n = 10
    for i in range(n+1):
        time.sleep(1)
        socketio.emit("progress", {"data": n - i})
    return 'solved!'
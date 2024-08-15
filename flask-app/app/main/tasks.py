import os
import time
from celery import shared_task
from flask_socketio import SocketIO

@shared_task(ignore_result=False)
def add_together(a: int, b: int) -> int:
    return a + b

@shared_task(ignore_result=False)
def test_task(sid: int, length: int) -> None:
    socketio = SocketIO(message_queue=os.environ.get("BROKER_URL", 'redis://localhost:6379/0'))
    for i in range(length+1):
        time.sleep(1)
        socketio.emit("progress", {"data": length - i, "max": length}, to=sid)
    return 'solved!'
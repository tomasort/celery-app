import time
from flask import current_app, render_template, request, Response
from flask_login import login_required
from celery.result import AsyncResult
from app.main import main
from app.main.tasks import add_together, test_task
from app import db, socketio

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/secret')
@login_required
def secrets():
    return render_template('secrets.html')

@main.route('/progressbar')
def tasks():
    return render_template('progressbar.html')

@socketio.on('start-task')
def start_task(data):
    result = test_task.delay(request.sid, int(data['length']))
    return {"status": "Task started", "task_id": result.id}

@main.route('/addition')
def simple_task():
    return render_template('addition.html')

@main.post("/add")
def start_add() -> dict[str, object]:
    a = request.form.get("a", type=int)
    b = request.form.get("b", type=int)
    result = add_together.delay(a, b)
    return {"result_id": result.id}

@main.get("/result/<id>")
def task_result(id: str) -> dict[str, object]:
    result = AsyncResult(id)
    return {
        "ready": result.ready(),
        "successful": result.successful(),
        "value": result.result if result.ready() else None,
    }
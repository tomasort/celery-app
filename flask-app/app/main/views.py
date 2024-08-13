from flask import current_app, render_template, request
from flask_login import login_required
from celery.result import AsyncResult
from app.main import main
from app.main.tasks import add_together
from app import db

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/secret')
@login_required
def secret():
    return render_template('secret.html')

@main.route('/test')
def test():
    return render_template('test.html')

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
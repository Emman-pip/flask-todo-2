from flask import Blueprint, render_template, request

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return render_template('pages/home.html')

@bp.route("/tasks")
def tasks():
    return render_template('pages/tasks.html')

@bp.route("/add-tasks")
def addTasks():
    return render_template('pages/addTasks.html')
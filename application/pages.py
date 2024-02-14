from flask import Blueprint, render_template, request
from application import db

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return render_template('pages/home.html')

@bp.route("/tasks")
def tasks():
    return render_template('pages/tasks.html')

@bp.route("/add-tasks", methods=("GET", "POST"))
def addTasks():
    if request.method == "POST":
        
        print(request.form["task"])
    return render_template('pages/addTasks.html')
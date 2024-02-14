from flask import Blueprint, render_template, request, current_app, redirect, url_for
# from application import Todo, db
import application

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return render_template('pages/home.html')

@bp.route("/tasks")
def tasks():
    tasks = application.Todo.query.all()
    return render_template('pages/tasks.html', tasks=tasks)

@bp.route("/add-tasks", methods=("GET", "POST"))
def addTasks():
    if request.method == "POST":
        task = request.form['task']
        description= request.form['desc']
        taskRecord = application.Todo(taskName=task, Description=description)
        
        application.db.session.add(taskRecord)
        application.db.session.commit()
        # return redirect(url_for('pages/addTasks'))
        
        
        print(request.form["task"])
    return render_template('pages/addTasks.html')
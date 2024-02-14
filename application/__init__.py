from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application import pages


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(pages.bp)

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    taskName = db.Column(db.String(100), nullable=False)
    Description = db.Column(db.Text)
    
    def __repr__(self):
        return f"<item#{self.id} {self.taskName}>"

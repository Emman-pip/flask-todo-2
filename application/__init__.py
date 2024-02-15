from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application import pages
import os
from dotenv import load_dotenv
from markupsafe import escape


app = Flask(__name__)
load_dotenv()
# username = os.getenv['MYSQL_ADDON_USER']
# password = os.getenv['MYSQL_ADDON_PASSWORD']
# host = os.getenv['MYSQL_ADDON_HOST']
# dbName = os.getenv['MYSQL_ADDON_DB']
# app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{escape(username)}:{escape(password)}@{escape(host)}/{escape(dbName)}'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('MYSQL_ADDON_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(pages.bp)

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    taskName = db.Column(db.String(100), nullable=False)
    Description = db.Column(db.Text)
    
    def __repr__(self):
        return f"<item#{self.id} {self.taskName}>"

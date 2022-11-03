from flask import render_template                         #std
from taskmanager import app, db                             #std the taskmanager is from env.py this line os.environ.setdefault("DB_URL", "postgresql:///taskmanager")   #std
from taskmanager.models import Category, Task           #std from models.py file import the classes created Category and Task



@app.route("/")                                         #std                                
def home():
    return render_template("tasks.html")               # first page is tasks.html ---
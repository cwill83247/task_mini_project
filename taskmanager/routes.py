from flask import render_template                         #std
from taskmanager import app, db                             #std


@app.route("/")                                         #std                                
def home():
    return render_template("base.html")
import os                                           #std
from flask import flask                             #std
from flask_sqlalchemy import SQLAlchemy             #std
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")       #std link to env.py
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")    #std link to env.py

import os                                           #std
from flask import Flask                             #std
from flask_sqlalchemy import SQLAlchemy             #std
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")       #std link to env.py

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")  # local
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)   #this just adds sql to the url due to some sort of bug...
    app.config["SQLALCHEMY_DATABASE_URI"] = uri  # heroku

db = SQLAlchemy(app)                                    #std SQLAlchment is whats imported above

from taskmanager import routes

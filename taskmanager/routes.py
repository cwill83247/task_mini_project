from flask import render_template ,request                         #std  the request is part of the form functionality
from taskmanager import app, db                             #std the taskmanager is from env.py this line os.environ.setdefault("DB_URL", "postgresql:///taskmanager")   #std
from taskmanager.models import Category, Task           #std from models.py file import the classes created Category and Task



@app.route("/")                                         #std                                
def home():
    return render_template("tasks.html")               # first page is tasks.html ---

@app.route("/categories")                                         #std                                
def categories():
    return render_template("categories.html")              

@app.route("/add_category", methods=["GET", "POST"])            #std   GET and POST are beacuse its a FORM                             
def add_category():
    if request.method == "POST":                                                ##part of post for category
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))                                    ##end of post for category    
    return render_template("add_category.html")              
from flask import render_template ,request, redirect , url_for                         #std  the request is part of the form functionality
from taskmanager import app, db                             #std the taskmanager is from env.py this line os.environ.setdefault("DB_URL", "postgresql:///taskmanager")   #std
from taskmanager.models import Category, Task           #std from models.py file import the classes created Category and Task



@app.route("/")                                         #std                                
def home():
    return render_template("tasks.html")               # first page is tasks.html ---

@app.route("/categories")                                         #std                                
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())  #so lists them by name
    return render_template("categories.html", categories=categories)          #  categories=categories  1st categories relates to categories.html template and 2nd is the variable declared above      

@app.route("/add_category", methods=["GET", "POST"])            #std   GET and POST are beacuse its a FORM                             
def add_category():
    if request.method =="POST":                                                ##part of post for category
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))                                    ##end of post for category    
    return render_template("add_category.html")              

@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])  ## we are passing back into the function here the id <int:category_id>
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)          ##this is a builtin SQLAlchemy method that tries to query base don whats passe din or it returns a 404 error
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)            #
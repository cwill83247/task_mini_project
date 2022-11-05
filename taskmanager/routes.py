from flask import render_template ,request, redirect , url_for                         #std  the request is part of the form functionality
from taskmanager import app, db                             #std the taskmanager is from env.py this line os.environ.setdefault("DB_URL", "postgresql:///taskmanager")   #std
from taskmanager.models import Category, Task           #std from models.py file import the classes created Category and Task



@app.route("/")                                         #std                                
def home():
    tasks = list(Task.query.order_by(Task.id).all())
    return render_template("tasks.html", tasks=tasks)

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


@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))           ##redirects back to the category function above, which then effectivley loads the categories page 

##my attempt
@app.route("/add_task", methods=["GET", "POST"])            #std   GET and POST are beacuse its a FORM                             
def add_task():
    categories = list(Category.query.order_by(Category.category_name).all())  ## this related to neededing the category
    if request.method =="POST":                                                
        task = Task(
            task_name=request.form.get("task_name"),                                        #set the forms attribute "task_name"
            task_description=request.form.get("task_description"),                                 #text field
            is_urgent=bool(True if request.form.get("is_urgent")else False),                           # boolean field 
            due_date=request.form.get("due_date"),
            category_id=request.form.get("category_id")                                      #   
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("home"))                                        
    return render_template("add_task.html", categories=categories)       


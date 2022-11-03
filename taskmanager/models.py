from taskmanager import db   #std


class Category(db.Model):                                                                       #std defining table schema
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)                       #must be unique name and not empty
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)     # tasks plural  this references the relationshp netween category and tasks and cascade links to the deletion and behavious when category deleted...

    def __repr__(self):                                                                         #std function required
        # __repr__ to represent itself in the form of a string
        return self.category_name


class Task(db.Model):                                                                           #std defining table schema
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)                                   #text field
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)                           # boolean field 
    due_date = db.Column(db.Date, nullable=False)                                            #   
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)   #foriegnkey field points to category class and id field category.id 
    #cascade option above means if category is deleted it will also delete the tasks associated with that category... 
    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Task: {1} | Urgent: {2}".format(                  
            self.id, self.task_name, self.is_urgent
        )
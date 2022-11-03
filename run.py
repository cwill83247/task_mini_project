import os                               #std
from taskmanager import app             #std    


if __name__ == "__main__":                  #std
    app.run(
        host=os.environ.get("IP"),               #getting from our env.py file 
        port=int(os.environ.get("PORT")),        #getting from our env.py file
        debug=os.environ.get("DEBUG")            #getting from our env.py file 
    )
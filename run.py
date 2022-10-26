import os                               #std
from taskmanager import app             #std    


if __name__ == "__main__":                  #std
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )
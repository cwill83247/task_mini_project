import os

os.environ.setdefault("IP", "0.0.0.0")       #std
os.environ.setdefault("PORT", "5000")                 #std
os.environ.setdefault("SECRET_KEY", "any_secret_key")          #std but change the secret key
os.environ.setdefault("DEBUG", "True")                          # std change to false for production
os.environ.setdefault("DEVELOPMENT", "True")                    # stsd change for prpdcution 
os.environ.setdefault("DB_URL", "postgresql:///taskmanager")   #std
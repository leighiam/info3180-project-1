from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

csrf = CSRFProtect()

# Config Values
ALLOWED_EXTENSIONS = {'png', 'jpg','jpeg', 'JPG'}
UPLOAD_FOLDER = './app/static/uploads'


app = Flask(__name__)
app.config['SECRET_KEY'] = "473bfaab3d010045ab39b0a7752c1b78"
csrf.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://leighiam:password123@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)


app.config.from_object(__name__)
from app import views

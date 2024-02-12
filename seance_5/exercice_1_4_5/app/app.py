from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from app.routes.erreur import erreur

app = Flask(
    __name__, 
    template_folder='templates',
    static_folder='statics')
app.config.from_object(Config)

erreur(app)
db = SQLAlchemy(app)

from .routes import generales, insertions
from dotenv import load_dotenv
load_dotenv()

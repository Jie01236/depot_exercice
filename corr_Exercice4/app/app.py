from flask import Flask
from .config import Config

app = Flask("factbook")
app.config.from_object(Config)
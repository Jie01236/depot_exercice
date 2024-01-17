from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jie:fanjie1016@localhost/yourdbname'

db = SQLAlchemy(app)

@app.route('/')
def index():
    return "Bienvenue!"

if __name__ == '__main__':
    app.run(debug=True)

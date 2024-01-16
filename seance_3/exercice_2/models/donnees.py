from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.VARCHAR(45), unique=True, nullable=False)
    user_surname = db.Column(db.VARCHAR(45), nullable=False)
    user_email = db.Column(db.VARCHAR(45), unique=True, nullable=False)
    user_password_hash = db.Column(db.TEXT, nullable=False)
    # 其他字段...
    user_inscription_date = db.Column(db.DATETIME, default=datetime.utcnow)

    # 定义与 Post 的关系
    posts = db.relationship('Post', backref='author', lazy=True)
    # 定义与 Comment 的关系
    comments = db.relationship('Comment', backref='author', lazy=True)
    # ...其他关系

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(45))
    # 其他字段...
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='posts')

User.posts = db.relationship('Post', order_by=Post.id, back_populates='user')

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    # 其他字段...
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    # 其他字段...

class CV(db.Model):
    __tablename__ = 'cv'
    id = db.Column(db.Integer, primary_key=True)
    # 其他字段...
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Competence(db.Model):
    __tablename__ = 'competence'
    id = db.Column(db.Integer, primary_key=True)
    # 其他字段...

class Skill(db.Model):
    __tablename__ = 'skill'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    competence_id = db.Column(db.Integer, db.ForeignKey('competence.id'), primary_key=True)
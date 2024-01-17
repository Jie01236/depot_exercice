from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

skill = db.Table("skill",
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('competence_id', db.Integer, db.ForeignKey('competences.id'), primary_key=True))

followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'), primary_key=True))

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), unique=True, nullable=False)
    firstname = db.Column(db.String(45), unique=True, nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    mail = db.Column(db.String(45), unique=True, nullable=False)
    password_hash = db.Column(db.TEXT, nullable=False)
    birthyear = db.Column(db.Integer, nullable=False)
    description = db.Column(db.TEXT, nullable=False)
    last_seen = db.Column(db.DateTime)
    linkedin = db.Column(db.TEXT, nullable=False)
    github = db.Column(db.TEXT, nullable=False)
    inscription_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    competences = db.relationship('Competences', secondary=skill, backref="users")

    followed = db.relationship('User',
                               secondary=followers,
                               primaryjoin=(followers.c.follower_id == id),
                               secondaryjoin=(followers.c.followed_id == id),
                               backref=db.backref('followers', lazy='dynamic'))

class Competences(db.Model):
    __tablename__ = 'competences'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(45), nullable=False)

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(45))
    message = db.Column(db.Text)
    date = db.Column(db.DateTime)
    indexation = db.Column(db.String(45))
    html = db.Column(db.Text)
    auteur_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    r_user = db.relationship('User', backref='posts', lazy=True) 

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text)
    date = db.Column(db.DateTime)
    html = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    auteur_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    r_post = db.relationship('Post', backref='comments', lazy=True)
    r_user = db.relationship('User', backref='comments', lazy=True) 

class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text)
    html = db.Column(db.Text)
    date = db.Column(db.DateTime)
    expediteur_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    destinaire_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    r_user = db.relationship('User', foreign_keys=[expediteur_id], backref='messages_e', lazy=True)
    r_user_2 = db.relationship('User', foreign_keys=[destinaire_id], backref='messages_d', lazy=True) 

class CV(db.Model):
    __tablename__ = 'cv'
    id = db.Column(db.Integer, primary_key=True)
    nom_poste = db.Column(db.Text)
    nom_emloyeur = db.Column(db.Text)
    ville = db.Column(db.String(45))
    annee_debut = db.Column(db.Integer, nullable=False)
    annee_fin = db.Column(db.Integer, nullable=False)
    description_poste = db.Column(db.Text)
    utilisateur_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    r_user = db.relationship('User', backref='cvs', lazy=True) 
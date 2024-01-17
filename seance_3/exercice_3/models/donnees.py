from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

affluence = db.Table('affluences',
    db.Column('affluent_id', db.Integer, db.ForeignKey('courseau.id'), primary_key=True),
    db.Column('effluent_id', db.Integer, db.ForeignKey('courseau.id'), primary_key=True))

traverse = db.Table("traverse",
    db.Column('coursEau', db.Integer, db.ForeignKey('courseau.id'), primary_key=True),
    db.Column('sousDivision', db.Integer, db.ForeignKey('sousdivision.id'), primary_key=True))

class CoursEau(db.Model):
    __tablename__ = 'courseau'
    id = db.Column(db.Integer, primary_key=True)
    denomination = db.Column(db.String(45), nullable=False)
    longueur = db.Column(db.Integer)
    typeid = db.Column(db.Integer, db.ForeignKey('typecourseau.id'))
    derniere_crue_majeure = db.Column(db.DateTime)

    affluence = db.relationship('CoursEau',
                               secondary=affluence,
                               primaryjoin=(affluence.c.affluent_id == id),
                               secondaryjoin=(affluence.c.effluent_id == id),
                               backref=db.backref('affluences', lazy='dynamic'))
    
    traverse = db.relationship('SousDivision', secondary=traverse, backref="courseaus")

class SousDivision(db.Model):
    __tablename__ = 'sousdivision'
    id = db.Column(db.Integer, primary_key=True)
    pays = db.Column(db.Integer, db.ForeignKey('pays.id'))
    type = db.Column(db.Integer, db.ForeignKey('typesousdivision.id'))
    denomination = db.Column(db.String(45), nullable=False)
    code_officiel = db.Column(db.String(12))

class TypeCoursEau(db.Model):
    __tablename__ = 'typecourseau'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(45), nullable=False)
    commentaire = db.Column(db.Text)

    r_courseau = db.relationship('courseau', backref='typecourseaus', lazy=True) 

class TypeSousDivision(db.Model):
    __tablename__ = 'typesousdivision'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(45), nullable=False)
    commentaire = db.Column(db.Text)

    r_sousdivision = db.relationship('sousdivision', backref='typesousdivisions', lazy=True)

class Pays(db.Model):
    __tablename__ = 'pays'
    id = db.Column(db.Integer, primary_key=True)
    denomination = db.Column(db.String(45), nullable=False)

    r_sousdivision = db.relationship('sousdivision', backref='pays', lazy=True)


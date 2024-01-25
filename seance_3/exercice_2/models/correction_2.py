from ..app import db
from datetime import datetime

# création de la table d'association des followers
followers = db.Table('followers',
                     db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
                     db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
                     )

# création de la table d'association des compétences des utilisateurs
skills = db.Table('skills',
                  db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                  db.Column('competence_id', db.Integer, db.ForeignKey('competences.competence_id'))
                  )


# création de la table user pour les informations sur l'utilisateur
class User( db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(45), index=True, unique=True)
    user_firstname = db.Column(db.String(45), index=True)
    user_surname = db.Column(db.String(45), index=True)

    user_mail = db.Column(db.Text, index=True, unique=True)
    user_password_hash = db.Column(db.Text)

    user_birthyear = db.Column(db.Integer)
    user_promotion_date = db.Column(db.String(45))
    user_description = db.Column(db.Text)
    user_last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    user_inscription_date = db.Column(db.DateTime, default=datetime.utcnow)

    user_linkedin = db.Column(db.Text)
    user_github = db.Column(db.Text)

    # jointures avec les autres tables
    posts = db.relationship("Post",
                            backref='auteur',
                            lazy='dynamic')

    comments = db.relationship('Comment',
                               backref='auteur',
                               lazy='dynamic')

    cvs = db.relationship("CV",
                          backref='utilisateur',
                          lazy='dynamic')

    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

    competences = db.relationship('Competences',
                                  secondary=skills,
                                  backref=db.backref('utilisateur', lazy='dynamic'),
                                  lazy='dynamic')

# création de la table des posts
class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    post_titre = db.Column(db.String(45))
    post_message = db.Column(db.Text)
    post_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    post_indexation = db.Column(db.String(45))
    html = db.Column(db.Text)

    # jointures avec les autres tables
    post_auteur = db.Column(db.Integer, db.ForeignKey('user.id'))

    comments = db.relationship('Comment',
                               backref='post',
                               lazy='dynamic')

# création de la table des commentaires
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment_message = db.Column(db.Text)
    comment_html = db.Column(db.Text)
    comment_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    comment_auteur = db.Column(db.Integer, db.ForeignKey('user.id'))
    comment_post = db.Column(db.Integer, db.ForeignKey('post.post_id'))

# création de la table des messages privés: idéalement, il faudrait en faire une table many-to-many comme skills
class Message(db.Model):
    message_id = db.Column(db.Integer, primary_key=True)
    message_message = db.Column(db.Text)
    message_html = db.Column(db.Text)
    message_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    message_expediteur_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    message_destinataire_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    message_expediteur = db.relationship('User',
                                         foreign_keys=[message_expediteur_id])
    message_destinataire= db.relationship('User',
                                          foreign_keys=[message_destinataire_id])

# création de la table des expériences professionnelles
class CV(db.Model):
    cv_id = db.Column(db.Integer, primary_key=True)
    cv_nom_poste = db.Column(db.Text)
    cv_nom_employeur = db.Column(db.Text)
    cv_ville = db.Column(db.String(45))
    cv_annee_debut = db.Column(db.Integer)
    cv_annee_fin = db.Column(db.Integer)
    cv_description_poste = db.Column(db.Text)

    cv_utilisateur = db.Column(db.Integer, db.ForeignKey('user.id'))

# création de la table des compétences
class Competences(db.Model):
    competences_id = db.Column(db.Integer, primary_key=True)
    competences_label = db.Column(db.String(45))
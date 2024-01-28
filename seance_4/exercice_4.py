from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from model import User
query = User.query.filter(User.name.ilike('%luc%'))

query = User.query.filter(~User.identifiant.in_([2, 5, 9]))

from sqlalchemy import func
query = User.query.filter(func.regexp_matches(User.name, '^.*(L|l)uc.*'))

query = User.query.filter(func.regexp_replace(User.name, '^.*(L|l)uc.*', 'Simplement Luc'))
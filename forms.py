from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(64), index=True, unique=True, nullable=False)
    score = db.Column(db.Integer, nullable=False)
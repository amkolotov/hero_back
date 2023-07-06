from core.db import db


class Hero(db.Model):
    """Модель героя"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

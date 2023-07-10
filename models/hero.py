from sqlalchemy import Column, Integer, String

from app import db


class Hero(db.Model):
    """Модель героя"""
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    def to_dict(self):
        return dict(
            [
                (k, getattr(self, k)) for k in self.__dict__.keys()
                if not k.startswith("_")
            ]
        )

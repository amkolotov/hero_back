from core.extensions import db


class Hero(db.Model):
    """Модель героя"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    @classmethod
    def get_list(cls, name):
        if name:
            return cls.query.filter(cls.name.like("%"+name+"%")).all()
        return cls.query.all()

    @classmethod
    def get(cls, hero_id):
        return db.get_or_404(Hero, hero_id)

    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise

    @classmethod
    def update(cls, hero_id, **kwargs):
        hero = db.get_or_404(Hero, hero_id)
        try:
            for key, value in kwargs.items():
                setattr(hero, key, value)
            db.session.commit()
            return hero
        except Exception:
            db.session.rollback()
            raise

    @classmethod
    def delete(cls, hero_id):
        hero = db.get_or_404(Hero, hero_id)
        db.session.delete(hero)
        db.session.commit()
        return hero

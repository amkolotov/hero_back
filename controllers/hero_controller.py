from flask import request
from flask_sqlalchemy import SQLAlchemy

from models.hero import Hero


class HeroController:

    _db: SQLAlchemy

    def __init__(self, db: SQLAlchemy):
        self._db = db

    def list_heroes(self):
        name = request.args.get('name')
        hero_list = self._db.session.query(Hero).order_by('name').all()
        if name:
            hero_list = self._db.session.query(Hero).filter(
                Hero.name.like("%"+name+"%")
            ).order_by('name').all()
        return [hero.to_dict() for hero in hero_list]

    def hero_detail(self, hero_id: int = 1):
        hero = self._db.get_or_404(Hero, hero_id)
        return hero.to_dict()

    def add_hero(self):
        try:
            hero = Hero(**request.json)
            self._db.session.add(hero)
            self._db.session.commit()
            self._db.session.refresh(hero)
            return hero.to_dict(), 201

        except Exception:
            self._db.session.rollback()
            raise

    def update_hero(self, hero_id: int):
        hero = self._db.get_or_404(Hero, hero_id)
        try:
            for key, value in request.json.items():
                setattr(hero, key, value)
            self._db.session.commit()
            self._db.session.refresh(hero)
            return hero.to_dict()

        except Exception:
            self._db.session.rollback()
            raise

    def delete_hero(self, hero_id: int):
        try:
            hero = self._db.get_or_404(Hero, hero_id)
            self._db.session.delete(hero)
            self._db.session.commit()
            return '', 204

        except Exception:
            self._db.session.rollback()
            raise

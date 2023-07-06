import json

from flask import Blueprint

from apps.hero.models import Hero
from core.db import db

bp = Blueprint('hero', __name__, url_prefix='/hero')


@bp.route('/')
def users():
    hero_list = list(
        db.session.execute(db.select(Hero).order_by(Hero.name)).scalars()
    )
    return json.dumps(
        [
            {'id': hero_item.id, 'username': hero_item.username}
            for hero_item in hero_list
        ]
    )

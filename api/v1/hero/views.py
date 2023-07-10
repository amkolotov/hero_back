from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from apps.hero.models import Hero
from apps.hero.schemas import HeroSchema


hero_bp = Blueprint('hero', __name__, url_prefix='/api/v1/heroes')


@hero_bp.route('/', methods=['GET'])
def list_heroes():
    name = request.args.get('name')
    return jsonify(HeroSchema(many=True).dump(Hero.get_list(name)))


@hero_bp.route("/<hero_id>")
def hero_detail(hero_id):
    return jsonify(HeroSchema().dump(Hero.get(hero_id)))


@hero_bp.route("/", methods=['POST'])
def add_hero():
    schema = HeroSchema()
    try:
        hero = schema.load(request.json)
        hero.add()
        return jsonify(schema.dump(hero)), 201

    except ValidationError as e:
        return jsonify(e.messages), 400


@hero_bp.route("/<hero_id>", methods=['PUT'])
def update_hero(hero_id):
    schema = HeroSchema()
    try:
        schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    hero = Hero.update(hero_id, **request.json)

    return jsonify(schema.dump(hero))


@hero_bp.route("/<hero_id>", methods=['DELETE'])
def delete_hero(hero_id):
    Hero.delete(hero_id)
    return '', 204

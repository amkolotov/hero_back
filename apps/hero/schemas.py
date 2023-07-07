from apps.hero.models import Hero

from core.extensions import ma


class HeroSchema(ma.SQLAlchemyAutoSchema):
    """Схема данных героя"""

    class Meta:
        model = Hero
        load_instance = True

    id = ma.auto_field(dump_only=True)
    name = ma.auto_field()

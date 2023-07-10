import importlib

from connexion import Resolver
from flask_sqlalchemy import SQLAlchemy


class HeroResolver(Resolver):
    _db: SQLAlchemy

    def __init__(self, db: SQLAlchemy):
        super().__init__()
        self._db = db

    def resolve_function_from_operation_id(self, operation_id):
        module, controller_name, operation = operation_id.rsplit('.', 2)
        controller_module = importlib.import_module(module)
        controller_cls = getattr(controller_module, controller_name)
        controller = controller_cls(db=self._db)
        return getattr(controller, operation)

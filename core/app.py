from flask import Flask
from decouple import config

from api.v1.hero.views import bp
from core.db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config(
    'DB_URI',
    default='sqlite:///api.db'
)

db.init_app(app)
db.app = app

app.register_blueprint(bp)

with app.app_context():
    db.create_all()


@app.teardown_request
def shutdown_session(exception=None):
    db.session.remove()


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return "Server Error!", 500


@app.errorhandler(404)
def not_found_error(error):
    return "Not found", 404

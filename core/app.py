from decouple import config, Csv
from flask import Flask
from flask_cors import CORS

from api.v1.hero.views import hero_bp
from core.extensions import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config(
    'DB_URII',
    default='sqlite:///api.db'
)

db.init_app(app)

app.url_map.strict_slashes = False
app.register_blueprint(hero_bp)

with app.app_context():
    db.create_all()

cors = CORS(app, resources={
    r"/*": {"origins": config('CORS_ALLOWED_ORIGINS', cast=Csv(), default='')}
})


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

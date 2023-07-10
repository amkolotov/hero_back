import connexion
from decouple import config, Csv
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from routes import HeroResolver

db = SQLAlchemy()

app = connexion.FlaskApp(__name__)
app.app.url_map.strict_slashes = False

app.app.config['SQLALCHEMY_DATABASE_URI'] = config(
    'DB_URI',
    default='sqlite:///api.db'
)
db.init_app(app.app)

with app.app.app_context():
    from models.hero import Hero
    db.create_all()

cors = CORS(app.app, resources={
    r"/*": {"origins": config('CORS_ALLOWED_ORIGINS', cast=Csv(), default='')}
})

app.add_api('swagger/main.yaml', resolver=HeroResolver(db=db))


@app.app.teardown_request
def shutdown_session(exception=None):
    db.session.remove()

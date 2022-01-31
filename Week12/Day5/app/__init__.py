import flask
import flask_migrate
import flask_sqlalchemy

from config import Config

app = flask.Flask(__name__)  # Remember: __name__ is the name of the file where the code is written

app.config.from_object(Config)

db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

from app import routes, error_handlers, models

from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # Make sure flask_sqlalchemy is installed in your environment
from flask_migrate import Migrate
from flask_cors import CORS
from backend.config.config import Config

# Initialize Flask extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    # Register blueprints
    from backend.api import gurus, sessions, users
    app.register_blueprint(gurus.bp)
    app.register_blueprint(sessions.bp)
    app.register_blueprint(users.bp)

    return app

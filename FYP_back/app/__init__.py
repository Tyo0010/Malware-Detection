from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config

db = SQLAlchemy()
migrate = Migrate(db)

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)
    app_context = app.app_context()
    app_context.push()

    # Initialize DB
    db.init_app(app)

    # Initialize migrate
    migrate.init_app(app, db)

    from app.views import blueprint as views_bp
    app.register_blueprint(views_bp)

    from app.errors import blueprint as errors_bp
    app.register_blueprint(errors_bp)

    db.create_all()
    db.session.commit()

    return app
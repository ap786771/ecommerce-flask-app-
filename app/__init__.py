from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.secret_key = "your-secret-key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../instance/app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app

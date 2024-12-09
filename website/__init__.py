from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import pymysql
import logging

# Configure PyMySQL to work as MySQLdb
pymysql.install_as_MySQLdb()

# Load environment variables from a .env file
load_dotenv()

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    """
    Factory function to create and configure the Flask application.
    """
    app = Flask(__name__)

    app.logger.setLevel(logging.INFO)

    # Load configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('JAWSDB_URL', 'sqlite:///app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True

    # Initialize extensions with the app
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.signin'  # Redirect to signin if not logged in

    # Import and register blueprints
    from .models import Admin
    from .views import main_blueprint
    from .auth import auth_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return Admin.query.get(int(user_id))

    with app.app_context():
        try:
            db.create_all()
            app.logger.info("Database tables created successfully or already exist")
        except Exception as e:
            app.logger.warning(f"Note during database initialization: {str(e)}")
            pass
    return app
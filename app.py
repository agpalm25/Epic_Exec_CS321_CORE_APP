"""Main application module for the CA application system."""

import os
from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager

from models import db, Admin
from views import main_blueprint
from auth import auth_blueprint

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret keyyyyy'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('JAWSDB_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'auth.signin'


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID for Flask-Login."""
    return Admin.query.get(int(user_id))


# Register blueprint for routes
app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

import os
from flask import Flask
from models import db, Admin

app = Flask(__name__)

# Get the absolute path to the database file
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'instance', 'mydatabase.db')

# Configure the SQLAlchemy database URI with an absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy instance with the Flask app
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print(f"Database tables created successfully at {db_path}")

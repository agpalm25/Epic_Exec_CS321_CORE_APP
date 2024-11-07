from flask import Flask
from models import db, Admin, ApplicantInformation
from views import main_blueprint
from auth import auth_blueprint
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret keyyyyy'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'auth.signin'

@login_manager.user_loader
def load_user(id):
    return Admin.query.get(int(id))

# Register blueprint for routes
app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint)

with app.app_context():
    db.create_all() 

if __name__ == '__main__':
    app.run(debug=True)

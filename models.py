from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class Admin(UserMixin, db.Model):

    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<Admin {self.email}>'


class Applicant(db.Model):

    __tablename__ = 'applications'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(6))
    email = db.Column(db.String(30))

    last_name = db.Column(db.String(20))
    first_name = db.Column(db.String(20))
    preferred_name = db.Column(db.String(20))
    pronouns = db.Column(db.String(20))
    phone_number = db.Column(db.String(10))

    cur_residence = db.Column(db.Integer)
    cur_room_number = db.Column(db.String(3))
    cur_position = db.Column(db.Integer)
    study_abroad = db.Column(db.Integer)
    prev_leadership = db.Column(db.Integer)

    major_1 = db.Column(db.String(20))
    major_2 = db.Column(db.String(20))
    minor_1 = db.Column(db.String(20))
    minor_2 = db.Column(db.String(20))
    gpa = db.Column(db.Float)

    next_year_standing = db.Column(db.String(40))
    anticipated_month_year_grad = db.Column(db.Integer)
    time_commitments = db.Column(db.String(20))

    text_response_1 = db.Column(db.String(2000))
    add_info = db.Column(db.String(2000))

    # insert something here for a resume !
    # resume = db.Column(db.String(20))

    healthy_housing_interest = db.Column(db.Integer)
    substance_housing_interest = db.Column(db.Integer)
    intercultural_housing_interest = db.Column(db.Integer)
    staff_interest_1 = db.Column(db.Integer)
    staff_interest_2 = db.Column(db.Integer)
    pop_interest = db.Column(db.Integer)

    signature = db.Column(db.String(30))

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

class Appointment(db.Model):
    __tablename__ = 'appointment'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String, db.ForeignKey('applicant_information.student_id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)

    applicant = db.relationship('ApplicantInformation', back_populates='appointment')

    def __repr__(self):
        return f'<Appointment for {self.student_id} on {self.date} at {self.time}>'

class ApplicantInformation(db.Model):
    __tablename__ = 'applicant_information'
    
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    preferred_name = db.Column(db.String, nullable=True)
    pronouns = db.Column(db.String, nullable=False)
    student_id = db.Column(db.String, unique=True, nullable=False)
    current_hall = db.Column(db.String, nullable=False)
    current_room_number = db.Column(db.String, nullable=False)
    current_email = db.Column(db.String, nullable=False)
    current_phone_number = db.Column(db.String, nullable=False)
    returning_ca_or_new_ca = db.Column(db.String, nullable=False)
    major_1 = db.Column(db.String, nullable=False)
    major_2 = db.Column(db.String, nullable=True)
    minor_1 = db.Column(db.String, nullable=True)
    minor_2 = db.Column(db.String, nullable=True)
    class_year = db.Column(db.String, nullable=False)
    cumulative_gpa = db.Column(db.Float, nullable=False)
    leadership_experience = db.Column(db.PickleType, nullable=False)
    application_status = db.Column(db.String, default='Submitted', nullable=False)
    assessment_status = db.Column(db.String, default='Yet to Be Assessed', nullable=False)

    # Relationships
    preferences = db.relationship('ApplicantPreferences', backref='applicant', uselist=False)
    additional_info = db.relationship('AdditionalInformation', backref='applicant', uselist=False)
    appointment = db.relationship('Appointment', back_populates='applicant', uselist=False)

    def get_interview_status(self):
        if self.appointment:
            return f"Scheduled for {self.appointment.date} at {self.appointment.time}"
        return "Yet To Schedule"

    def __repr__(self):
        return f'<ApplicantInformation {self.first_name} {self.last_name}>'

class ApplicantPreferences(db.Model):
    __tablename__ = 'applicant_preferences'
    
    id = db.Column(db.Integer, primary_key=True)
    substance_free_housing_interest = db.Column(db.Integer, nullable=False)
    healthy_colby_interest = db.Column(db.String, nullable=False)
    population_interest = db.Column(db.String, nullable=False)
    staff_interest = db.Column(db.PickleType, nullable=False) 
    illc_interest = db.Column(db.String, nullable=False)
    student_id = db.Column(db.String, db.ForeignKey('applicant_information.student_id'), nullable=False)

class AdditionalInformation(db.Model):
    __tablename__ = 'additional_information'
    
    id = db.Column(db.Integer, primary_key=True)
    why_ca = db.Column(db.String, nullable=False)
    additional_comments = db.Column(db.String, nullable=True)
    student_id = db.Column(db.String, db.ForeignKey('applicant_information.student_id'), nullable=False)

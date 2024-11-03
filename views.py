from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Appointment
from datetime import datetime

# Create a blueprint for routes
main_blueprint = Blueprint('main', __name__)


@main_blueprint.route("/")
def home():
    return render_template("home.html")

@main_blueprint.route("/requirements")
def requirements():
    return render_template("requirements_page.html")

@main_blueprint.route("/appointment")
def appointment():
    return render_template("appointment.html")

@main_blueprint.route("/ca-info")
def ca_info():
    return render_template("ca_info.html")

@main_blueprint.route("/application")
def application():
    return render_template("application.html")

@main_blueprint.route("/UserHome")
def user_home():
    return render_template("UserHome.html")

@main_blueprint.route("/assessment")
def assessment():
    return render_template("assessment.html")

@main_blueprint.route("/apptSubmit", methods=['POST'])
def appt_submit():
    if request.method == 'POST':
        full_name = request.form.get('fullName')
        email = request.form.get('email')
        date_str = request.form.get('apptDate')
        time_str = request.form.get('apptTime')

        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            time = datetime.strptime(time_str, '%H:%M').time()

            new_appointment = Appointment(full_name=full_name, email=email, date=date, time=time)
            db.session.add(new_appointment)
            db.session.commit()

            flash('Appointment scheduled successfully!', 'success')
            return redirect(url_for('main.appointment'))
        except ValueError:
            flash('Invalid date or time format. Please try again.', 'error')
            return redirect(url_for('main.appointment'))

    return redirect(url_for('main.appointment'))

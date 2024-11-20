"""Views module for the CA application system."""

import logging
from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from sqlalchemy import or_, and_
from sqlalchemy.exc import SQLAlchemyError

from models import (
    db, Appointment, ApplicantInformation, ApplicantPreferences, AdditionalInformation
)
from email_sender import (
    send_application_confirmation_email, send_interview_confirmation_email
)

# Create a blueprint for routes
main_blueprint = Blueprint('main', __name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@main_blueprint.route("/")
def home():
    """Render the home page."""
    return render_template("home.html")


@main_blueprint.route("/oldhome")
def home2():
    """Render the old home page."""
    return render_template("old_home.html")


@main_blueprint.route("/requirements")
def requirements():
    """Render the requirements page."""
    return render_template("requirements_page.html")


@main_blueprint.route("/appointment")
def appointment_page():
    """Render the appointment page."""
    return render_template("appointment.html")


@main_blueprint.route("/ca-info")
def ca_info():
    """Render the CA information page."""
    return render_template("ca_info.html")


@main_blueprint.route('/application', methods=['GET', 'POST'])
def application():
    """Handle the application submission process."""
    if request.method == 'POST':
        try:
            applicant_info = create_applicant_info(request.form)
            applicant_preferences = create_applicant_preferences(request.form)
            additional_info = create_additional_info(request.form)

            db.session.add(applicant_info)
            db.session.add(applicant_preferences)
            db.session.add(additional_info)
            db.session.commit()

            send_confirmation_email(request.form['email'])

            return redirect(url_for('main.ca_info'))

        except SQLAlchemyError as e:
            db.session.rollback()
            logger.error("Database error submitting application: %s", str(e))
            flash('Error submitting application. Please try again later.', 'danger')
        except ValueError as e:
            logger.error("Value error submitting application: %s", str(e))
            flash('Invalid input in application form. Please check your entries.', 'danger')
        except Exception as e:
            logger.error("Unexpected error submitting application: %s", str(e))
            flash('An unexpected error occurred. Please try again later.', 'danger')

        return redirect(url_for('main.application'))

    return render_template('application.html')


def create_applicant_info(form):
    """Create an ApplicantInformation object from form data."""
    return ApplicantInformation(
        last_name=form['last_name'],
        first_name=form['first_name'],
        preferred_name=form.get('preferred_name'),
        pronouns=form['pronouns'],
        student_id=form['student_id'],
        current_hall=form['cur_residence'],
        current_room_number=form['cur_room_num'],
        current_email=form['email'],
        current_phone_number=form['phone_number'],
        returning_ca_or_new_ca=form['cur_position'],
        major_1=form['major_1'],
        major_2=form.get('major_2'),
        minor_1=form.get('minor_1'),
        minor_2=form.get('minor_2'),
        class_year=form['next_year_standing'],
        cumulative_gpa=float(form['gpa']),
        leadership_experience=form.getlist('prev_leadership'),
        application_status='Submitted'
    )


def create_applicant_preferences(form):
    """Create an ApplicantPreferences object from form data."""
    return ApplicantPreferences(
        student_id=form['student_id'],
        substance_free_housing_interest=int(form['substance_housing_interest']),
        healthy_colby_interest=int(form['healthy_housing_interest']),
        population_interest=form['pop_interest'],
        staff_interest={
            "Alone": int(form['staff_interest_2']),
            "With a Partner": int(form['staff_interest_1'])
        },
        illc_interest=int(form['intercultural_housing_interest'])
    )


def create_additional_info(form):
    """Create an AdditionalInformation object from form data."""
    return AdditionalInformation(
        student_id=form['student_id'],
        why_ca=form['text_response_1'],
        additional_comments=form.get('add_info')
    )


def send_confirmation_email(email):
    """Send a confirmation email to the applicant."""
    try:
        send_application_confirmation_email(email)
        flash('Application submitted successfully! A confirmation email has been sent.', 'success')
    except (ConnectionError, TimeoutError) as e:
        logger.error("Network error sending confirmation email: %s", str(e))
        flash(
            'Application submitted successfully! '
            'However, there was an issue sending the confirmation email.',
            'warning'
        )
    except Exception as e:
        logger.error("Unexpected error sending confirmation email: %s", str(e))
        flash(
            'Application submitted successfully! '
            'However, there was an issue sending the confirmation email.',
            'warning'
        )


@login_required
@main_blueprint.route("/admin_homepage")
def admin_home():
    """Render the admin homepage with applicant search functionality."""
    search_query = request.args.get('search', '').strip()
    applicants = search_applicants(search_query)
    applicants_data = get_applicants_data(applicants)
    return render_template("admin_homepage.html", applicants=applicants_data, search_query=search_query)


def search_applicants(search_query):
    """Search for applicants based on the given query."""
    if not search_query:
        return ApplicantInformation.query.all()

    search_terms = search_query.split()
    if len(search_terms) > 1:
        return ApplicantInformation.query.filter(
            or_(
                and_(
                    ApplicantInformation.first_name.ilike(f'%{search_terms[0]}%'),
                    ApplicantInformation.last_name.ilike(f'%{search_terms[-1]}%')
                ),
                *[
                    or_(
                        ApplicantInformation.first_name.ilike(f'%{term}%'),
                        ApplicantInformation.last_name.ilike(f'%{term}%')
                    )
                    for term in search_terms
                ]
            )
        ).all()

    return ApplicantInformation.query.filter(
        or_(
            ApplicantInformation.first_name.ilike(f'%{search_query}%'),
            ApplicantInformation.last_name.ilike(f'%{search_query}%')
        )
    ).all()


def get_applicants_data(applicants):
    """Get formatted data for applicants."""
    applicants_data = []
    for applicant in applicants:
        appt = Appointment.query.filter_by(student_id=applicant.student_id).first()
        interview_status = (
            "Yet To Schedule" if not appt
            else f"Scheduled for {appt.date} at {appt.time}"
        )
        applicants_data.append({
            'first_name': applicant.first_name,
            'last_name': applicant.last_name,
            'student_id': applicant.student_id,
            'application_status': applicant.application_status,
            'interview_status': interview_status,
            'assessment_status': applicant.assessment_status
        })
    return applicants_data


@main_blueprint.route("/assessment/<string:student_id>")
def assessment_page(student_id):
    """Render the assessment page for a specific applicant."""
    applicant = ApplicantInformation.query.filter_by(student_id=student_id).first_or_404()
    return render_template("assessment.html", applicant=applicant)


@main_blueprint.route("/apptSubmit", methods=['POST'])
def appt_submit():
    """Handle appointment submission."""
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        date_str = request.form.get('apptDate')
        time_str = request.form.get('apptTime')

        applicant = ApplicantInformation.query.filter_by(student_id=student_id).first()

        if not applicant:
            flash('No application found for this student ID. Please submit an application first.', 'error')
            return redirect(url_for('main.appointment_page'))

        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            time = datetime.strptime(time_str, '%H:%M').time()

            new_appointment = Appointment(
                student_id=student_id,
                date=date,
                time=time
            )
            db.session.add(new_appointment)
            db.session.commit()

            send_interview_confirmation(applicant, date_str, time_str)

            return redirect(url_for('main.appointment_page'))
        except ValueError:
            flash('Invalid date or time format. Please try again.', 'error')
        except SQLAlchemyError as e:
            db.session.rollback()
            logger.error("Database error scheduling appointment: %s", str(e))
            flash('Error scheduling appointment. Please try again later.', 'danger')
        except Exception as e:
            logger.error("Unexpected error scheduling appointment: %s", str(e))
            flash('An unexpected error occurred. Please try again later.', 'danger')

    return redirect(url_for('main.appointment_page'))


def send_interview_confirmation(applicant, date_str, time_str):
    """Send interview confirmation email to the applicant."""
    try:
        send_interview_confirmation_email(
            applicant.current_email,
            f"{applicant.first_name} {applicant.last_name}",
            date_str,
            time_str
        )
        flash('Appointment scheduled successfully! A confirmation email has been sent.', 'success')
    except (ConnectionError, TimeoutError) as e:
        logger.error("Network error sending interview confirmation: %s", str(e))
        flash(
            'Appointment scheduled successfully! '
            'However, there was an issue sending the confirmation email.',
            'warning'
        )
    except Exception as e:
        logger.error("Unexpected error sending interview confirmation: %s", str(e))
        flash(
            'Appointment scheduled successfully! '
            'However, there was an issue sending the confirmation email.',
            'warning'
        )


@main_blueprint.route('/applicants')
def view_all_applicants():
    """Render a page with all applicants."""
    applicants = ApplicantInformation.query.all()
    applicants_data = get_applicants_data(applicants)
    return render_template('admin_homepage.html', applicants=applicants_data)


@login_required
@main_blueprint.route('/view_application/<string:student_id>')
def view_application(student_id):
    """Render a page to view a specific application."""
    applicant = ApplicantInformation.query.filter_by(student_id=student_id).first_or_404()
    preferences = ApplicantPreferences.query.filter_by(student_id=student_id).first()
    additional_info = AdditionalInformation.query.filter_by(student_id=student_id).first()
    return render_template(
        'view_application.html',
        applicant=applicant,
        preferences=preferences,
        additional_info=additional_info
    )


@login_required
@main_blueprint.route('/assess_applicant/<string:student_id>', methods=['GET', 'POST'])
def assess_applicant(student_id):
    """Handle applicant assessment."""
    applicant = ApplicantInformation.query.filter_by(student_id=student_id).first_or_404()

    if request.method == 'POST':
        assessment_status = request.form.get('assessment')
        applicant.assessment_status = assessment_status
        db.session.commit()
        flash('Assessment updated successfully', 'success')
        return redirect(url_for('main.admin_home'))

    return render_template('assess_applicant.html', applicant=applicant)

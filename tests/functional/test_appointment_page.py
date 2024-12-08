import pytest
from flask import url_for
from website.models import ApplicantInformation, Appointment

def test_appointment_page(client, app_context):
    response = client.get(url_for('main.appointment'))
    assert response.status_code == 200
    assert b"Schedule Interview Appointment" in response.data

def test_appointment_submission_success(client, db, app_context):
    # Creates an applicant for testing
    applicant = ApplicantInformation(
        student_id='12345',
        first_name='Test',
        last_name='User',
        current_email='test@example.com',
        current_hall='Test Hall',
        current_room_number='101',
        current_phone_number='1234567890',
        pronouns='He/Him',
        application_status='Submitted',
        assessment_status='Yet to Be Assessed',
        returning_ca_or_new_ca='New CA',
        major_1='Computer Science',
        class_year='2025',
        cumulative_gpa=3.5,
        leadership_experience='Some leadership experience'
    )
    db.session.add(applicant)
    db.session.commit()

    response = client.post(url_for('main.appt_submit'), data={
        'student_id': '12345',
        'apptDate': '2024-01-01',
        'apptTime': '14:00'
    }, follow_redirects=True)

    assert response.status_code == 200
    print("Response content:", response.data.decode())
    assert b'<div class="alert alert-success">Appointment scheduled successfully! A confirmation email has been sent.</div>' in response.data
    appointment = Appointment.query.filter_by(student_id='12345').first()
    assert appointment is not None
    assert appointment.date.strftime('%Y-%m-%d') == '2024-01-01'

def test_appointment_submission_no_applicant(client, db, app_context):
    # Attempts to submit an appointment for a non-existent applicant
    response = client.post(url_for('main.appt_submit'), data={
        'student_id': '99999',
        'apptDate': '2024-01-01',
        'apptTime': '14:00'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'<div class="alert alert-error">No application found for this student ID. Please submit an application first.</div>' in response.data
    appointment = Appointment.query.filter_by(student_id='99999').first()
    assert appointment is None

def test_flash_messages_display(client, app_context):
    # Test if flash messages are displayed correctly in the appointment page
    with client.session_transaction() as session:
        session['_flashes'] = [
            ('success', 'Test success message'),
            ('error', 'Test error message')
        ]
    response = client.get(url_for('main.appointment'))
    assert response.status_code == 200
    assert b'<div class="alert alert-success">Test success message</div>' in response.data
    assert b'<div class="alert alert-error">Test error message</div>' in response.data

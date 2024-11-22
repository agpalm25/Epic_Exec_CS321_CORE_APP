import pytest
from flask import url_for
from website.models import ApplicantInformation, Appointment

def test_appointment_page(client, app_context):
    response = client.get(url_for('main.appointment'))
    assert response.status_code == 200
    assert b"Schedule Interview Appointment" in response.data

def test_appointment_submission(client, db, app_context):
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

    # Submits an appointment here
    response = client.post(url_for('main.appt_submit'), data={
        'student_id': '12345',
        'apptDate': '2024-01-01',
        'apptTime': '14:00'
    }, follow_redirects=True)

    assert response.status_code == 200
    print("Response content:", response.data.decode())  
    assert b"Appointment scheduled successfully" in response.data or b"Thank you for scheduling your interview!" in response.data

    # Checks if an appointment was created in the database
    appointment = Appointment.query.filter_by(student_id='12345').first()
    assert appointment is not None
    assert appointment.date.strftime('%Y-%m-%d') == '2024-01-01'

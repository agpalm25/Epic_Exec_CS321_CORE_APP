import pytest
from flask import url_for
from website.models import ApplicantInformation

@pytest.mark.parametrize('student_id, expected_status', [
    ('existing_id', 200),
    ('non_existing_id', 404)
])
def test_assessment_page(client, db, app_context, student_id, expected_status):
    if student_id == 'existing_id':
        applicant = ApplicantInformation(
            student_id=student_id,
            first_name='Test',
            last_name='User',
            current_hall='Test Hall',
            current_room_number='101',
            current_phone_number='1234567890',
            pronouns='He/Him',
            current_email='test@example.com',
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

    response = client.get(url_for('main.assessment', student_id=student_id))
    assert response.status_code == expected_status

    if expected_status == 200:
        assert b"Assessment" in response.data

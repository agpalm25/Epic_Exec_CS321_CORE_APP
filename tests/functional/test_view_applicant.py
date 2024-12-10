''' author(s) : audrey palmer
    description : contains tests for the file view_applicant and its applicable
                 functions
    last edited : 12/9/24
'''

import pytest
from flask import url_for
from website.models import AdditionalInformation, Admin, ApplicantInformation, ApplicantPreferences

''' 
will set up database with an admin and applicant for other tests in the file
'''
def init_db(db) :

    db.session.query(ApplicantInformation).filter_by(student_id="132435").delete()
    db.session.query(ApplicantPreferences).filter_by(student_id="132435").delete()
    db.session.query(AdditionalInformation).filter_by(student_id="132435").delete()
    db.session.commit()

    test_applicant = ApplicantInformation(
        first_name = "good", 
        last_name = "applicant", 
        preferred_name = "gapicant", 
        pronouns = "all", 
        student_id = "132435", 
        current_hall = "2", 
        current_room_number = "101", 
        current_email = "gapicant@gmail.com", 
        current_phone_number = "1234567890", 
        returning_ca_or_new_ca = "0", 
        major_1 = "computer science", 
        major_2 = "terror", 
        minor_1 = "Mathematics", 
        minor_2 = None, 
        class_year = "senior", 
        cumulative_gpa = 3.7, 
        leadership_experience = ['0', '3'],  
        application_status = "Submitted",
        assessment_status = "Yet to Be Assessed"
    )
    test_applicant_preferences = ApplicantPreferences(
        substance_free_housing_interest = 3,
        healthy_colby_interest = "2",
        population_interest = "2",
        staff_interest = { "Alone" : "2", "With a Partner" : "3" },
        illc_interest = "2",
        student_id = "132435"

    )
    test_applicant_aInfo = AdditionalInformation(
        why_ca = "i think it would be fun :D",
        additional_comments = None,
        student_id = "132435"
    )

    db.session.add(test_applicant)
    db.session.commit()
    db.session.add(test_applicant_preferences)
    db.session.commit()
    db.session.add(test_applicant_aInfo)
    db.session.commit()

    return test_applicant



'''
maybe a but redundant, but a test file to make sure my db initialization
was successful
'''
def test_init_db(db) :
    '''
    GIVEN : our app and its context
    WHEN : init_db is called
    THEN : the applicable data is actually sent to the database in the
           proper spots
    '''

    applicant = init_db(db)

    applicant = ApplicantInformation.query.filter_by(student_id = "132435").first()
    assert applicant is not None
    assert applicant.major_2 == "terror"

    applicant_preferences = ApplicantPreferences.query.filter_by(student_id = "132435").first()
    assert applicant_preferences is not None
    assert applicant_preferences.substance_free_housing_interest == 3

    add_info = AdditionalInformation.query.filter_by(student_id = "132435").first()
    assert add_info is not None
    assert add_info.why_ca == "i think it would be fun :D"

'''
test that view_applicant will appear as expected
'''
def test_get_to_view_page(client, db) :

    response = client.get(f'view_application/132435')

    assert response.status_code == 200
    assert b'gapicant' in response.data
    assert b'1234567890' in response.data
    assert b'A Little Interested (2)' in response.data
    assert b'i think it would be fun :D' in response.data

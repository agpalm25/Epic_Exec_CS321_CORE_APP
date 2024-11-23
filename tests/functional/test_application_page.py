from website.models import ApplicantInformation

def test_application_access(test_client) :
    """
    GIVEN a Flask application configured for testing
    WHEN the '/application' page is requested (GET)
    THEN check the response is valid
    """

    response = test_client.get('/application')

    assert response.status_code == 200
    assert b'Community Advisor Application' in response.data
    assert b'Application, or for any questions, please contact' in response.data
    assert b'Major' in response.data
    assert b'submit' in response.data


def test_application_successful_applicant(test_client) :
    """
    GIVEN a Flask application has been configured for testing and has a visible
          landing page
    WHEN an applicant submits an application that meets qualifications
    THEN the user is redireted to the correct page
    """

    response = test_client.post('/application', data=dict(first_name = "Test", last_name = "Person", pronouns = "they/them", student_id = 123456 , cur_residence = 11, cur_room_num = 111, email = "toper27@colby.edu", phone_number = "1234567890", cur_position = 1, major_1 = "Smiling", next_year_standing = "other", anticipated_month_year_grad = "6", study_abroad = "0", gpa = 4.0, time_commitments = "None", prev_leadership = "9", text_response_1 = "hi!", healthy_housing_interest = "5", substance_housing_interest = "5", intercultural_housing_interest = "5", staff_interest_1 = "5", staff_interest_2 = "5", pop_interest = "0", signature = "Test Person"), follow_redirects = True)
    
    assert response.status_code == 200
    assert b'What does a CA do?' in response.data

def test_application_almost_failure(test_client) :
    """
    GIVEN a Flask application has been configured for testing and has a visible
          landing page
    WHEN an applicant submits an application that does not meet qualifications
         (already existing student id)
    THEN the user is redireted to the correct page (they just go back to the application page)
    """

    response = test_client.post('/application', data=dict(first_name = "Test", last_name = "Person", pronouns = "they/them", student_id = 123456 , cur_residence = 11, cur_room_num = 111, email = "toper27@colby.edu", phone_number = "1234567890", cur_position = 1, major_1 = "Smiling", next_year_standing = "other", anticipated_month_year_grad = "6", study_abroad = "0", gpa = 4.0, time_commitments = "None", prev_leadership = "9", text_response_1 = "hi!", healthy_housing_interest = "5", substance_housing_interest = "5", intercultural_housing_interest = "5", staff_interest_1 = "5", staff_interest_2 = "5", pop_interest = "0", signature = "Test Person"), follow_redirects = True)
    response = test_client.post('/application', data=dict(first_name = "TestTwo", last_name = "PersonTwo", pronouns = "they/them", student_id = 123456 , cur_residence = 11, cur_room_num = 111, email = "toper26@colby.edu", phone_number = "34567890", cur_position = 1, major_1 = "Smiling", next_year_standing = "other", anticipated_month_year_grad = "6", study_abroad = "0", gpa = 4.0, time_commitments = "None", prev_leadership = "9", text_response_1 = "hi!", healthy_housing_interest = "5", substance_housing_interest = "5", intercultural_housing_interest = "5", staff_interest_1 = "5", staff_interest_2 = "5", pop_interest = "0", signature = "Test Person"), follow_redirects = True)

    assert response.status_code == 200
    assert b'Major' in response.data

def test_application_home_link(test_client) :
    """
    GIVEN a Flask application has been configured for testing and has
          a viewable landing page
    WHEN the home button is hit (/ is requested (GET))
    THEN check the response is valid
    """

    response = test_client.get('/application')
    response = test_client.get('/', follow_redirects = True)

    assert response.status_code == 200
    assert b'campus? Would you like' in response.data



""" i would've loved to test this but it would require implementation o
    something that could interact with javascript :( """
# def test_application_form_invisible_upon_request_until_arrow_click(test_client) :
#     """
#     GIVEN a Flask application has been configured for testing and has a visible
#           landing page
#     WHEN the arrow is clicked...
#     THEN the form portion is shown and then text portion is made invisible
#     """

#     response = test_client.get('/application')



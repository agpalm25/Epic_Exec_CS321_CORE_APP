def test_get_assess_app_page(test_client) :
    """
    GIVEN a working Flask admin home page
    WHEN an admin clicks on a user's assess applicant link
    THEN the correct page is returned
    """
    response = test_client.post('/application', data=dict(first_name = "Test", last_name = "Person", pronouns = "they/them", student_id = 123456 , cur_residence = 11, cur_room_num = 111, email = "toper27@colby.edu", phone_number = "1234567890", cur_position = 1, major_1 = "Smiling", next_year_standing = "other", anticipated_month_year_grad = "6", study_abroad = "0", gpa = 4.0, time_commitments = "None", prev_leadership = "9", text_response_1 = "hi!", healthy_housing_interest = "5", substance_housing_interest = "5", intercultural_housing_interest = "5", staff_interest_1 = "5", staff_interest_2 = "5", pop_interest = "0", signature = "Test Person"), follow_redirects = True)
    response = test_client.get('/assess_applicant/123456')

    assert response.status_code == 200
    assert b'Test' in response.data
    assert b'123456' in response.data
    assert b'Overall Assessment' in response.data

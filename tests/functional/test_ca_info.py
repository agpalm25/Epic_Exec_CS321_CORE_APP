def test_ca_info_access(test_client) :
    """
    GIVEN a Flask application configured for testing
    WHEN the '/ca_page is requested (GET)
    THEN check the response is valid
    """

    response = test_client.get('/ca_info')

    assert response.status_code == 200 
    assert b'What does a CA do?' in response.data
    assert b'Responsibilities' in response.data
    assert b'Training and Development' in response.data
    assert b'Testimonials from CAs' in response.data
    assert b'Perks and Compensation' in response.data
    assert b'Click here to see the requirements to be a CA :]' in response.data

def test_ca_info_requirements_link(test_client) :
    """
    GIVEN a Flask application has been configured for testing and has
          a viewable landing page
    WHEN the requirements link is hit (/requirements is requested (GET))
    THEN check the response is valid
    """

    response = test_client.get('/ca_info')
    response = test_client.get('/requirements', follow_redirects = True)

    assert response.status_code == 200
    assert b'Requirements' in response.data
    assert b'Minimum GPA of 2.5' in response.data

def test_ca_info_home_link(test_client) :
    """
    GIVEN a Flask application has been configured for testing and has
          a viewable landing page
    WHEN the home button is hit (/ is requested (GET))
    THEN check the response is valid
    """

    response = test_client.get('/ca_info')
    response = test_client.get('/', follow_redirects = True)

    assert response.status_code == 200
    assert b'campus? Would you like' in response.data
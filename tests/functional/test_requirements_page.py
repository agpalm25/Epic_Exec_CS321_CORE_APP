from flask import url_for

def test_requirements_page(client, app_context):
    response = client.get(url_for('main.requirements'))
    assert response.status_code == 200
    assert b"Requirements" in response.data

def test_home_page(client):
    """Test the home page renders correctly with expected content."""
    response = client.get("/")
    assert response.status_code == 200

    assert b"Apply to become a CA!" in response.data
    assert b"Would you like to help create community on campus?" in response.data
    assert b"What does a CA do?" in response.data
    assert b"Application" in response.data
    assert b"Make an Appointment" in response.data
    assert b"Admin Sign-In" in response.data

    assert b"alt=\"Mariner Residence\"" in response.data
    assert b"alt=\"Averill Residence\"" in response.data
    assert b"alt=\"Drummond Residence\"" in response.data
    assert b"alt=\"West-Quad Residence\"" in response.data

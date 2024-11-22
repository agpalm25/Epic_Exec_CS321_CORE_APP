from website.models import Admin
from website import db

def test_signup_page(client):
    response = client.get('/signup')
    assert response.status_code == 200
    assert b'Admin Signup' in response.data

def test_signin_page(client):
    response = client.get('/signin')
    assert response.status_code == 200
    assert b'Sign In' in response.data

def test_successful_signup(client, app_context, session):
    response = client.post('/signup', data={
        'email': 'newadmin@colby.edu',
        'password': 'testpassword123'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Sign In' in response.data
    
    user = Admin.query.filter_by(email='newadmin@colby.edu').first()
    assert user is not None
    assert user.check_password('testpassword123')

def test_duplicate_signup(client, app_context, session):
    """Test signing up with an email that already exists"""
    # Create first user
    admin = Admin(email='test@colby.edu')
    admin.set_password('testpassword123')
    session.add(admin)
    session.commit()
    
    # Try duplicate signup
    response = client.post('/signup', data={
        'email': 'test@colby.edu',
        'password': 'differentpassword'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Sign In' in response.data
    
    # Verify only one user exists
    users = Admin.query.filter_by(email='test@colby.edu').all()
    assert len(users) == 1

def test_successful_signin(client, app_context, session):
    """Test successful login"""
    admin = Admin(email='unique_test@colby.edu')
    admin.set_password('testpassword123')
    session.add(admin)
    session.commit()
    
    response = client.post('/signin', data={
        'email': 'unique_test@colby.edu',
        'password': 'testpassword123'
    }, follow_redirects=True)
    
    assert response.status_code == 200


def test_invalid_signin(client):
    """Test login with wrong credentials"""
    response = client.post('/signin', data={
        'email': 'wrong@colby.edu',
        'password': 'wrongpassword'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Sign In' in response.data

def test_forgot_password(client):
    """Test forgot password page"""
    response = client.get('/forgot-password')
    assert response.status_code == 200
    assert b'Forgot password functionality coming soon!' in response.data
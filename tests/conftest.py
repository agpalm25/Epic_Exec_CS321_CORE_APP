import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from website import create_app, db as _db


@pytest.fixture(scope='session')
def app():
    """Create the Flask application."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SERVER_NAME'] = 'localhost.localdomain'
    return app

@pytest.fixture(scope='session')
def db(app):
    """Set up the database."""
    with app.app_context():
        _db.create_all() 
        yield _db
        _db.drop_all() 

@pytest.fixture(scope='function')
def client(app):
    """Provide a test client."""
    return app.test_client()

@pytest.fixture(scope='function')
def session(app, db):
    """
    Provide a database session for a test function,
    rolling back changes after the test.
    """
    with app.app_context():
        connection = db.engine.connect()
        transaction = connection.begin()

        db.session.bind = connection
        yield db.session

        transaction.rollback()
        connection.close()
        db.session.remove()

@pytest.fixture(scope='function')
def app_context(app):
    """Provide an app context for a test function."""
    with app.app_context():
        yield

@pytest.fixture(scope='module')
def test_client() :

    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        yield test_client 
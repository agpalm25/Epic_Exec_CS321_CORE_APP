import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from website import create_app, db as _db

@pytest.fixture(scope='session')
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SERVER_NAME'] = 'localhost.localdomain'  
    return app

@pytest.fixture(scope='session')
def db(app):
    with app.app_context():
        _db.create_all()
        yield _db
        _db.drop_all()

@pytest.fixture(scope='function')
def client(app):
    return app.test_client()

@pytest.fixture(scope='function')
def session(db):
    connection = db.engine.connect()
    transaction = connection.begin()
    session = db.create_scoped_session()

    yield session

    transaction.rollback()
    connection.close()
    session.remove()

@pytest.fixture(scope='function')
def app_context(app):
    with app.app_context():
        yield

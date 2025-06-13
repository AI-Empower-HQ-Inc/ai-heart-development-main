import os
import tempfile
import pytest
from backend import create_app
from backend.models.database import db

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # Create a temporary file to isolate the database for each test
    db_fd, db_path = tempfile.mkstemp()
    
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': f'sqlite:///{db_path}',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'SECRET_KEY': 'test',
        'OPENAI_API_KEY': 'test-key'
    })

    # Create the database and load test data
    with app.app_context():
        db.create_all()
        yield app

    # Cleanup
    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """A test CLI runner for the app."""
    return app.test_cli_runner()

@pytest.fixture
def auth_header():
    """Fixture to provide mock authentication headers."""
    return {'Authorization': 'Bearer test-token'}

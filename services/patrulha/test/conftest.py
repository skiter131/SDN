import pytest
from src.app import app

@pytest.fixture(scope="module")
def app():
    """
    Instance of main flask app
    """
    return app
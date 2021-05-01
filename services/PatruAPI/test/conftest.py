import pytest
from src.app import APP

@pytest.fixture(scope="module")
def app():
    """
    Instance of main flask app
    """
    return APP
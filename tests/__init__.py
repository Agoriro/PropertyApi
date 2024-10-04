import pytest
from src.database import Database
from src.config import DatabaseConfig

@pytest.fixture
def db_config():
    return DatabaseConfig(
        host='localhost',
        port=3306,
        database='test_habi_db',
        user='test_user',
        password='test_password'
    )

@pytest.fixture
def mock_db(mocker):
    return mocker.Mock(spec=Database)
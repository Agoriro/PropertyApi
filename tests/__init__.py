import pytest
from src.database import Database
from src.config import DatabaseConfig

@pytest.fixture
def db_config():
    """
    Fixture que proporciona la configuración de la base de datos para las pruebas.

    Retorna:
    --------
    DatabaseConfig
        Un objeto DatabaseConfig con los detalles de conexión a la base de datos de prueba.
    """
    return DatabaseConfig(
        host='localhost',
        port=3306,
        database='test_habi_db',
        user='test_user',
        password='test_password'
    )

@pytest.fixture
def mock_db(mocker):
    """
    Fixture que proporciona una instancia mock de la clase Database utilizando el mocker de pytest.

    Parámetros:
    -----------
    mocker : pytest-mock
        Inyección automática del objeto mocker proporcionado por la librería pytest-mock.

    Retorna:
    --------
    mocker.Mock
        Un objeto mock que simula la clase Database.
    """
    return mocker.Mock(spec=Database)

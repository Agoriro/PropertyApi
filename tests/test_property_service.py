import unittest
from unittest.mock import MagicMock
from src.services.property_service import PropertyService
from src.configdb import Database
from src.models.property import Property

class TestPropertyService(unittest.TestCase):
    """
    Clase de prueba para el servicio PropertyService.

    Esta clase contiene pruebas unitarias para el servicio PropertyService que
    interactúa con la base de datos a través de la clase Database.

    Atributos:
    ----------
    mock_db : MagicMock
        Simulación de la clase Database para evitar interacciones reales con la base de datos.
    property_service : PropertyService
        Instancia del servicio PropertyService, que utiliza la base de datos simulada.

    Métodos:
    --------
    setUp()
        Configura el entorno de prueba creando mocks y la instancia del servicio.
    test_get_properties_no_filters()
        Prueba el método get_properties sin filtros.
    test_get_properties_with_filters()
        Prueba el método get_properties con filtros específicos.
    """
    def setUp(self):
        """
        Configura el entorno de prueba inicial.

        Este método se ejecuta antes de cada prueba, creando una instancia mock
        de la clase Database y una instancia del PropertyService utilizando la base de datos mockeada.
        """
        self.mock_db = MagicMock(spec=Database)
        self.property_service = PropertyService(self.mock_db)

    def test_get_properties_no_filters(self):
        """
        Prueba el método get_properties cuando no se aplican filtros.

        Simula una respuesta de la base de datos con un solo inmueble y verifica
        que la salida del servicio contenga una lista de objetos Property correctamente
        instanciados.

        Asserciones:
        ------------
        - La longitud del resultado debe ser 1.
        - El primer elemento del resultado debe ser una instancia de Property.
        - El ID y el estado del primer inmueble deben ser los esperados.
        """
        mock_data = [
            {
                "id": 1,
                "address": "Test Address",
                "city": "Test City",
                "price": 100000,
                "description": "Test Description",
                "year": 2020,
                "status": "en_venta"
            }
        ]
        self.mock_db.execute_query.return_value = mock_data

        result = self.property_service.get_properties({})
        
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], Property)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].status, "en_venta")

    def test_get_properties_with_filters(self):
        """
        Prueba el método get_properties cuando se aplican filtros específicos.

        Simula una respuesta de la base de datos con un inmueble que coincide con los
        filtros proporcionados (ciudad, año, estado) y verifica que el resultado sea
        correcto.

        Asserciones:
        ------------
        - La longitud del resultado debe ser 1.
        - El inmueble devuelto debe tener la ciudad, el año y el estado especificados en los filtros.
        """
        mock_data = [
            {
                "id": 2,
                "address": "Filtered Address",
                "city": "Bogota",
                "price": 200000,
                "description": "Filtered Description",
                "year": 2021,
                "status": "pre_venta"
            }
        ]
        self.mock_db.execute_query.return_value = mock_data

        filters = {"city": "Bogota", "year": 2021, "status": "pre_venta"}
        result = self.property_service.get_properties(filters)
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].city, "Bogota")
        self.assertEqual(result[0].year, 2021)
        self.assertEqual(result[0].status, "pre_venta")

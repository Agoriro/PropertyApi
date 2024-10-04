import unittest
from unittest.mock import MagicMock
from src.services.property_service import PropertyService
from src.configdb import Database
from src.models.property import Property

class TestPropertyService(unittest.TestCase):
    def setUp(self):
        self.mock_db = MagicMock(spec=Database)
        self.property_service = PropertyService(self.mock_db)

    def test_get_properties_no_filters(self):
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
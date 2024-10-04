import json
from typing import Dict, Any

class PropertyHandler:
    def __init__(self, property_service):
        self.property_service = property_service

    def handle_get_properties(self, query_params: Dict[str, Any]) -> Dict[str, Any]:
        filters = {}
        
        if 'year' in query_params:
            try:
                filters['year'] = int(query_params['year'][0])
            except ValueError:
                return {"error": "Invalid year format"}, 400
        
        if 'city' in query_params:
            filters['city'] = query_params['city'][0]
        
        if 'status' in query_params:
            status = query_params['status'][0]
            if status not in ['pre_venta', 'en_venta', 'vendido']:
                return {"error": "Invalid status"}, 400
            filters['status'] = status

        properties = self.property_service.get_properties(filters)
        
        response_data = [
            {
                "address": p.address,
                "city": p.city,
                "price": p.price,
                "description": p.description,
                "status": p.status_name
            }
            for p in properties
        ]
        
        return {"properties": response_data}, 200
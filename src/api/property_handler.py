"""
Property Handler Module

Este módulo proporciona la clase PropertyHandler que actúa como intermediario
entre las solicitudes HTTP y el servicio de propiedades, manejando la lógica
de procesamiento de parámetros y formato de respuestas.

Classes:
    PropertyHandler: Maneja las solicitudes relacionadas con propiedades inmobiliarias.

Dependencies:
    - json
    - typing
"""
import json
from typing import Dict, Any

class PropertyHandler:
    """
    Maneja las solicitudes relacionadas con propiedades inmobiliarias.

    Esta clase actúa como una capa intermedia entre las solicitudes HTTP y el
    servicio de propiedades, procesando los parámetros de consulta y formateando
    las respuestas.

    Attributes:
        property_service: Una instancia del servicio que maneja las operaciones
                         de base de datos para las propiedades.
    """
    def __init__(self, property_service):
        """
        Inicializa el manejador de propiedades.

        Args:
            property_service: Una instancia del servicio de propiedades que
                             realizará las operaciones reales de base de datos.
        """
        self.property_service = property_service

    def handle_get_properties(self, query_params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Maneja las solicitudes GET para obtener propiedades con filtros.

        Procesa los parámetros de consulta y los convierte en filtros que pueden
        ser utilizados por el servicio de propiedades.

        Args:
            query_params: Un diccionario de parámetros de consulta donde las claves
                         son strings y los valores son listas de strings.
                         Parámetros soportados:
                         - year: Año de la propiedad (int)
                         - city: Ciudad donde se encuentra la propiedad (string)
                         - status: Estado de la propiedad (string: 'pre_venta',
                                  'en_venta', o 'vendido')

        Returns:
            Una tupla que contiene:
            - Un diccionario con la respuesta formateada
            - Un código de estado HTTP (200 para éxito, 400 para error de validación)

        """
        filters = {}

        # Procesar el año
        if 'year' in query_params:
            try:
                filters['year'] = int(query_params['year'][0])
            except ValueError:
                return {"error": "Invalid year format"}, 400

        # Procesar la ciudad
        if 'city' in query_params:
            filters['city'] = query_params['city'][0]

        # Procesar el estado
        if 'status' in query_params:
            status = query_params['status'][0]
            if status not in ['pre_venta', 'en_venta', 'vendido']:
                return {"error": "Invalid status"}, 400
            filters['status'] = status
            
        # Obtener y formatear las propiedades
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

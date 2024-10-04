"""
HTTP Server Module for Property API

Este módulo implementa un servidor HTTP personalizado para manejar solicitudes
relacionadas con propiedades inmobiliarias. Define un manejador de solicitudes
personalizado y una función para crear el servidor.

Classes:
    RequestHandler: Manejador personalizado para procesar solicitudes HTTP
Functions:
    create_server: Crea y configura una instancia del servidor HTTP
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs

class RequestHandler(BaseHTTPRequestHandler):
    """
    Manejador personalizado para procesar solicitudes HTTP relacionadas con propiedades.

    Attributes:
        property_handler: Una instancia del manejador de propiedades que procesa
                         la lógica de negocio para las solicitudes.

    Methods:
        do_GET: Maneja las solicitudes HTTP GET
    """
    def __init__(self, *args, property_handler=None, **kwargs):

        """
        Inicializa el manejador de solicitudes.

        Args:
            *args: Argumentos posicionales que se pasan al constructor padre
            property_handler: Instancia del manejador de propiedades
            **kwargs: Argumentos de palabra clave que se pasan al constructor padre
        """
        
        self.property_handler = property_handler
        super().__init__(*args, **kwargs)

    def do_GET(self):
        """
        Maneja las solicitudes HTTP GET.

        Este método procesa las siguientes rutas:
        - /properties: Retorna una lista de propiedades basada en los parámetros
                      de consulta proporcionados

        La respuesta siempre será en formato JSON.
        """
        parsed_path = urlparse(self.path)
        
        if parsed_path.path == '/properties':
            # Procesar solicitud para el endpoint /properties
            query_params = parse_qs(parsed_path.query)
            response_data, status_code = self.property_handler.handle_get_properties(query_params)
            
            self.send_response(status_code)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode())
        else:
            # Manejar rutas no encontradas
            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Not found"}).encode())

def create_server(host: str, port: int, property_handler) -> HTTPServer:
    """
    Crea y configura una instancia del servidor HTTP.

    Args:
        host: La dirección IP o hostname donde el servidor escuchará
        port: El puerto en el que el servidor escuchará
        property_handler: Instancia del manejador de propiedades que procesará
                         la lógica de negocio para las solicitudes

    Returns:
        HTTPServer: Una instancia configurada del servidor HTTP
    """
    def handler(*args):
        """
        Closure para crear instancias del RequestHandler con el property_handler.
        """
        RequestHandler(*args, property_handler=property_handler)
    
    server = HTTPServer((host, port), handler)
    return server

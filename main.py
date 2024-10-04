"""
Property API Server Launcher

Este script inicia un servidor API para manejar operaciones relacionadas con propiedades.
Configura la conexión a la base de datos, inicializa los servicios necesarios y
arranca el servidor HTTP.

Dependencias:
    - Las variables de entorno deben estar configuradas para la conexión a la base de datos
    - Los módulos src.config, src.configdb, src.services.property_service, y src.api.* 
      deben estar disponibles

Uso:
    Ejecutar directamente este script:
    $ python main.py

"""

from src.config import DatabaseConfig
from src.configdb import Database
from src.services.property_service import PropertyService
from src.api.property_handler import PropertyHandler
from src.api.server import create_server
import os

def main():
    """
    Función principal que inicializa y ejecuta el servidor de la API de propiedades.

    Esta función realiza las siguientes operaciones:
    1. Configura la conexión a la base de datos usando variables de entorno
    2. Inicializa la conexión a la base de datos
    3. Configura el servicio de propiedades y el manejador de la API
    4. Inicia el servidor HTTP y lo mantiene en ejecución

    Variables de entorno utilizadas:
        DB_HOST: El host de la base de datos (default: 'localhost')
        DB_PORT: El puerto de la base de datos (default: 3306)
        DB_NAME: El nombre de la base de datos (default: 'db')
        DB_USER: El usuario de la base de datos (default: 'user')
        DB_PASSWORD: La contraseña de la base de datos (default: 'password')
    """
    
    db_config = DatabaseConfig(
        host: str = os.getenv('DB_HOST', 'localhost')
        port: int = int(os.getenv('DB_PORT', 3306))
        database: str = os.getenv('DB_NAME', 'db')
        user: str = os.getenv('DB_USER', 'user')
        password: str = os.getenv('DB_PASSWORD', 'password')
    )

    # Inicialización
    try:
        # Establecer conexión a la base de datos
        database = Database(db_config)
        database.connect()

        # Inicializar servicios y manejadores
        property_service = PropertyService(database)
        property_handler = PropertyHandler(property_service)

        # Configuración del servidor
        port = 8000   # TODO: Considerar hacer este valor configurable
        server = create_server('', port, property_handler)

        print(f"Server running on port {port}")
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
    finally:
        # Asegurar que la conexión a la base de datos se cierre apropiadamente
        database.disconnect()

if __name__ == "__main__":
    main()

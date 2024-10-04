from src.config import DatabaseConfig
from src.configdb import Database
from src.services.property_service import PropertyService
from src.api.property_handler import PropertyHandler
from src.api.server import create_server
import os

def main():
    # Configuración
    db_config = DatabaseConfig(
        host: str = os.getenv('DB_HOST', 'localhost')
        port: int = int(os.getenv('DB_PORT', 3306))
        database: str = os.getenv('DB_NAME', 'db')
        user: str = os.getenv('DB_USER', 'user')
        password: str = os.getenv('DB_PASSWORD', 'password')
    )

    # Inicialización
    try:
        database = Database(db_config)
        database.connect()
        
        property_service = PropertyService(database)
        property_handler = PropertyHandler(property_service)

        # Configuración del servidor
        port = 8000
        server = create_server('', port, property_handler)

        print(f"Server running on port {port}")
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
    finally:
        database.disconnect()

if __name__ == "__main__":
    main()
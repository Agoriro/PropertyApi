"""
Database Configuration Module

Este módulo define la configuración de la base de datos utilizando variables de entorno
con valores por defecto. Utiliza dataclasses para una representación limpia y tipada
de la configuración.

Classes:
    DatabaseConfig: Dataclass que encapsula la configuración de la base de datos.

Dependencies:
    - dataclasses
    - os

Environment Variables:
    DB_HOST: Host de la base de datos
    DB_PORT: Puerto de la base de datos
    DB_NAME: Nombre de la base de datos
    DB_USER: Usuario de la base de datos
    DB_PASSWORD: Contraseña de la base de datos

"""
from dataclasses import dataclass
import os

@dataclass
class DatabaseConfig:
    host: str = os.getenv('DB_HOST', 'localhost')
    port: int = int(os.getenv('DB_PORT', 3306))
    database: str = os.getenv('DB_NAME', 'db')
    user: str = os.getenv('DB_USER', 'user')
    password: str = os.getenv('DB_PASSWORD', 'password')






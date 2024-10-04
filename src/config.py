from dataclasses import dataclass
import os

@dataclass
class DatabaseConfig:
    host: str = os.getenv('DB_HOST', 'localhost')
    port: int = int(os.getenv('DB_PORT', 3306))
    database: str = os.getenv('DB_NAME', 'db')
    user: str = os.getenv('DB_USER', 'user')
    password: str = os.getenv('DB_PASSWORD', 'password')






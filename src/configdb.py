import mysql.connector
from mysql.connector import Error
from .config import DatabaseConfig

class Database:
    """
    Clase Database que gestiona la conexión con una base de datos MySQL, así como la ejecución de consultas.

    Atributos:
    -----------
    config : DatabaseConfig
        Configuración de la base de datos (host, puerto, nombre, usuario, contraseña).
    connection : mysql.connector.connection_cext.CMySQLConnection
        Conexión activa a la base de datos MySQL, o None si no se ha conectado.
    """
    def __init__(self, config: DatabaseConfig):
        """
        Constructor de la clase Database.

        Parámetros:
        -----------
        config : DatabaseConfig
            Objeto de configuración que contiene la información de la base de datos.
        """
        self.config = config
        self.connection = None

    def connect(self):
        """
        Establece la conexión a la base de datos MySQL utilizando los parámetros de configuración.
        
        Si la conexión falla, se lanza una excepción y se muestra un mensaje de error.
        
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.config.host,
                port=self.config.port,
                database=self.config.database,
                user=self.config.user,
                password=self.config.password
            )
        except Error as e:
            print(f"Error connecting to MySQL database: {e}")
            raise

    def disconnect(self):
        """
        Cierra la conexión a la base de datos si está activa.
        """
        if self.connection and self.connection.is_connected():
            self.connection.close()

    def execute_query(self, query: str, params: tuple = None):
        """
        Ejecuta una consulta SQL en la base de datos.

        Parámetros:
        -----------
        query : str
            Consulta SQL a ejecutar.
        params : tuple, opcional
            Parámetros a utilizar en la consulta SQL. Por defecto es None.

        Retorna:
        --------
        list[dict]
            Resultado de la consulta SQL como una lista de diccionarios.
        """
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            return cursor.fetchall()
        finally:
            cursor.close()

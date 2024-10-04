# Habi Microservicios - Propiedades y Likes

## Tecnologías Utilizadas

### Lenguaje Principal
- **Python 3.10**

### Base de Datos
- **MySQL**
  
### Bibliotecas
- **mysql-connector-python**

### Servidor HTTP
- **http.server (Biblioteca estándar de Python)**

### Pruebas
- **unittest (Biblioteca estándar de Python)**
- **unittest.mock**


### Como se abordara el desarrollo

- Se decide abordar el proyecto abordando por pasos que serán los siguientes:
-   **Creación de repositorio.
-   **Documentación en README
-   **Creación entorno virtual
-   **Creación de conexión a base de datos
-   **Creación servicio de propiedades
-   **Creación pruebas unitarias
-   **Creación servicio de likes
-   **Propuestas en el readme



## Endpoints

### Propiedades
```
GET /properties
Filtros opcionales:
- year (int)
- city (string)
- status (string: pre_venta, en_venta, vendido)
```


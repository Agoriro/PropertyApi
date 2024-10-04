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
-   Creación de repositorio.
-   Documentación en README
-   Creación entorno virtual
-   Creación de conexión a base de datos
-   Creación servicio de propiedades
-   Creación pruebas unitarias
-   Creación servicio de likes
-   Propuestas en el readme



## Endpoints

### Propiedades
```
GET /properties
Filtros opcionales:
- year (int)
- city (string)
- status (string: pre_venta, en_venta, vendido)
```

# Modelo entidad relación de los likes

![image](https://github.com/user-attachments/assets/f7f1f54d-765d-4802-a274-b3fb1f022ab8)

Este modelo permite registrar los likes otorgados por usuarios registrados a propiedades específicas. Es importante definir un índice único con los campos user_id y property_id para evitar duplicidades en los likes. Este modelo soporta futuras funcionalidades como:

-  Obtener las propiedades que han sido marcadas con like por un usuario.
-  Saber qué usuarios han dado like a una propiedad específica.
-  Generar rankings de propiedades más populares (por cantidad de likes).
-  Filtrar la información por fecha en la que se dio el like.



# Propuesta mejora modelo entidad relación 

![image](https://github.com/user-attachments/assets/a68fa28f-f060-42f5-bf7c-4bdbdffa2e38)

Se propone agregar varias tablas catalogo para lograr normalizar la base de datos y mejorar la velocidad de las consultas.

#### Tablas 
- cities
- departaments
- countries
- type
- features
- properties_features
- type_features

#### Explicación de tablas
-   **cities, departaments, countries**: Estas tablas permiten normalizar los datos, mejorando la velocidad de las consultas mediante búsquedas por ID (entero) en lugar de texto. Además, facilitan la creación de endpoints     que permitan filtrar inmuebles por departamento o país.
-   **type**: Clasifica los tipos de propiedades (ej. Apartamento, Casa, Bodega, Parqueadero). Esto mejora las búsquedas por tipo y garantiza integridad referencial.
-   **features, properties_features, type_features**: Estas tablas refuerzan la capacidad de búsqueda personalizada al almacenar información detallada sobre las características de las propiedades (ej. número de habitaciones, garaje, cocina). Así se puede realizar una búsqueda precisa y eficiente.

## **Recomendaciones Adicionales**

Además de la normalización, se recomienda optimizar las búsquedas mediante la creación de procedimientos almacenados e índices en las tablas. Esto permitirá que la base de datos precompile los planes de ejecución, mejorando considerablemente los tiempos de consulta. 

También se recomienda paginar las consultas para que así el set de registros devueltos en la consulta sea menor y la experiencia de usuario mejore.



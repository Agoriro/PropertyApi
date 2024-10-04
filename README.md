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

## Modelo entidad relación de los likes

![image](https://github.com/user-attachments/assets/f7f1f54d-765d-4802-a274-b3fb1f022ab8)

Con este modelo se busca que se puedan registrar los likes, dados por los usuarios registrados, hay que tener en cuenta que se debe crear un unique index con los campos de 
user_id y property_id para que un usuario solo le pueda dar like a una propiedad, con este modelo se proyecta a futuro, poder generar información como:

- el usuario a que propiedades le dio like
- Que usuarios le dieron like a una propiedad en especifico
- Ranking de propiedades por like
- Toda esta información también se podrá filtrar por la fecha en la que se dio el like


## Propuesta mejora modelo entidad relación 

![image](https://github.com/user-attachments/assets/a68fa28f-f060-42f5-bf7c-4bdbdffa2e38)




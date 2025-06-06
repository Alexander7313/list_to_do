# To Do List

## Descripción

Este proyecto implementa una aplicación CRUD utilizando Python como lenguaje principal, SQLAlchemy como ORM, y SQLite como base de datos. Está estructurado siguiendo una arquitectura en capas tipo MVC para facilitar el mantenimiento y la escalabilidad del código.

## Tabla de Contenidos

- Descripción  
- Tecnologías Utilizadas  
- Estructura del Proyecto  
- Funcionalidades  
- Pruebas Unitarias  
- Repositorio  
- Autores

## Tecnologías Utilizadas

- **Python 3.10+**
- **SQLite** como sistema de base de datos.
- **SQLAlchemy** para la capa ORM.
- **unittest** para pruebas unitarias.

## Estructura del Proyecto
proyecto/

├── models/ # Entidades y esquemas de la base de datos

├── repositories/ # Capa de acceso a datos (CRUD)

├── services/ # Lógica de negocio

├── tests/ # Pruebas unitarias

├── data/ # Contiene la base de datos SQLite

│ └── database.db

├── main.py # Punto de entrada de la aplicación

└── requirements.txt # Lista de dependencias


## Funcionalidades

- Operaciones CRUD completas para las entidades definidas.
- Validaciones básicas (campos obligatorios, tipos de datos).
- Base de datos persistente en `./data/database.db`.

## Pruebas Unitarias

- Implementadas con `unittest`.
- Uso de base de datos en memoria (`sqlite:///:memory:`).
- Casos de prueba de éxito y error para cada operación CRUD.

## Repositorio

[https://github.com/Alexander7313/list_to_do.git]

## Autores

| Nombre completo                      | Rol            |
|--------------------------------------|----------------|
| Alexander Nelson Landa Rojas         | Desarrollador  |
| Arce Curi Rodrigo Vladimir           | Desarrollador  |
| Gamarra Curi Gianmarco               | Desarrollador  |
| Gutiérrez Taipe Luis Alberto         | Desarrollador  |
| Salvador Rivera Bruce Joshua         | Desarrollador  |
| Tucto Ubaldo Ricardo David           | Desarrollador  |


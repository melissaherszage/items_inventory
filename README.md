# Tp Final Python Data Applications

# Analisis de productos de la categoria Consolas y Videojuegos 

## Introducción

Este proyecto utiliza Docker Compose para levantar airflow y fue diseñado para automatizar la extracción diaria de datos de items de consolas y videojuegos desde la API de MercadoLibre. Utilizando herramientas como Apache Airflow, Redshift, y Docker, el pipeline recopila información sobre precios, stocks y si los productos son nuevos o usados. Los datos luego son transformados y cargados en Redshift para facilitar su modelado y análisis, permitiendo un estudio continuo del mercado de videojuegos.

## Caracteristicas del proyecto

- Extracción de datos: Se conecta diariamente a la API de MercadoLibre.
- Carga en Redshift: Los datos transformados son cargados en Redshift para consultas y análisis futuros.
- Transformación de datos: Los datos son limpiados y preparados para análisis.

## Set Up

Es requisito tener Docker y Docker Compose instalados.

1. Clonar el repositorio:
```git clone https://github.com/melissaherszage/items_inventory.git```

2. Navegar al directorio del proyecto:
```cd items_inventory```

3. Levantar los servicios usando Docker Compose:
```docker compose up -d```

4. Acceder a la interfaz de Airflow para monitorear el pipeline y verificar la ejecución de los DAGs.
```http://localhost:8080```
- Username: airflow
- Password: airflow

5. Configura una nueva conexión en Airflow:
- Ir a Admin -> Connections.
- Crea una nueva conexión con los siguientes detalles:
    - Connection Id: redshift_default
    - Connection Type: Postgres (ojo! no es redshift)
    - Host: redshift-pda-cluster.cnuimntownzt.us-east-2.redshift.amazonaws.com
    - Database: pda
    - Port: 5439
    - User: 2024_melissa_herszage
    - Password: Contactarme a meliherszage@gmail.com para obtener la contraseña.

## Funte de datos

Se utilizo un codigo de python para traer data de la API de Mercado Libre
```https://api.mercadolibre.com/sites/MLA/categories```

## Estructura

- dags/: Contiene los DAGs (Definiciones de flujo de trabajo) de Airflow.
- python_files/: Contiene todos los archivos de python necesarios para ejecutar las tareas del dag de ELT
    - lib/: Contiene scripts Python de soporte para conexiones y transformaciones de datos.
- sql_files/: Almacena los archivos SQL para la transformación y carga de datos.
- docker-compose.yml: Define los servicios de Docker necesarios para levantar el entorno de Airflow

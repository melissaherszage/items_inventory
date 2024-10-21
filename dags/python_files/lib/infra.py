import os
import psycopg2

# Conexión a bases de datos de redshift

def database_connection():
    conn = psycopg2.connect(
        host=os.getenv('REDSHIFT_HOST'),
        dbname=os.getenv('REDSHIFT_DB'),
        user=os.getenv('REDSHIFT_USER'),
        password=os.getenv('REDSHIFT_PASSWORD'),
        port=os.getenv('REDSHIFT_PORT', 5439)  # Default to 5439 if not provided
    )
    return conn
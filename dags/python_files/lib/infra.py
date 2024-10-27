from airflow.providers.postgres.hooks.postgres import PostgresHook

# Conexión a bases de datos de redshift

def database_connection(conn_id: str = 'redshift_default'):
    """
    Establece una conexión a una base de datos PostgreSQL mediante un hook de Airflow.

    Args:
        conn_id (str): ID de la conexión de Airflow para PostgreSQL. 
        Por defecto es 'redshift_default'.

    Returns:
        psycopg2.extensions.connection: Objeto de conexión a la base de datos.
    """

    hook = PostgresHook(postgres_conn_id=f'{conn_id}')

    conn = hook.get_conn()

    return conn

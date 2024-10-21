from airflow.providers.postgres.hooks.postgres import PostgresHook

# Conexión a bases de datos de redshift

def database_connection(conn_id: str = 'redshift_default'):

    hook = PostgresHook(postgres_conn_id=f'{conn_id}')

    conn = hook.get_conn()

    return conn
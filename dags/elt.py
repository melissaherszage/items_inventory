import os
import datetime
from airflow import DAG
from datetime import timedelta
from airflow.utils.task_group import TaskGroup
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from python_files.l1.items.items import insert_items
from python_files.l1.prices.prices import insert_prices
from python_files.lib.sql_folder import get_dag_sql_files
from python_files.lib.get_dag_id import get_dag_id


# Defino el DAG 

DAG_ID = get_dag_id(__file__)

DEFAULT_ARGS = {
    "owner": 'mherszage',
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
    'postgres_conn_id': "redshift_default",
    'email_on_failure': False,
    'email_on_retry': False,
}

with DAG(
        dag_id=DAG_ID,
        default_args=DEFAULT_ARGS,
        dagrun_timeout=timedelta(minutes=15),
        start_date=datetime.datetime(2024, 10, 16),
        schedule_interval='0 12 * * *',
        tags=['inserts'],
        catchup=False
) as dag:

    with TaskGroup(group_id="extract_load_data") as extract_load_data:

        create_table_items = PostgresOperator(
            task_id='create_table_items',
            sql='sql_files/l1/items/create_table.sql'
            )
        
        create_table_prices = PostgresOperator(
            task_id='create_table_prices',
            sql='sql_files/l1/prices/create_table.sql'
            )

        insert_items_task = PythonOperator(
            task_id='insert_items',
            python_callable=insert_items
        )

        insert_prices_task = PythonOperator(
            task_id='insert_prices',
            python_callable=insert_prices
        )

        [create_table_items, create_table_prices] >> insert_items_task >> insert_prices_task

    with TaskGroup(group_id="transform_data") as transform_data:

        sql_paths = get_dag_sql_files(dag_folder='l2')

        for sql_path in sql_paths:
            task_id_sql = os.path.basename(sql_path).replace(".sql", "")  # Crear un task_id basado en el nombre del archivo
            
            PostgresOperator(
            task_id=f"run_{task_id_sql}",
            #postgres_conn_id='redshift_default',
            sql=sql_path,
        )

extract_load_data >> transform_data


import os
import datetime
from airflow import DAG
from datetime import timedelta
#from python_files.lib.infra import get_redshift_connection
from airflow.utils.task_group import TaskGroup
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from python_files.items.items import insert_items
from python_files.prices.prices import insert_prices

# Defino el DAG 

DAG_ID = os.path.basename(__file__).replace(".py", "")

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

    with TaskGroup(group_id="extract_data") as extract_data:

        create_table_items = PostgresOperator(
            task_id='create_table_items',
            sql='sql_files/items/create_table.sql'
            )
        
        create_table_prices = PostgresOperator(
            task_id='create_table_prices',
            sql='sql_files/prices/create_table.sql'
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
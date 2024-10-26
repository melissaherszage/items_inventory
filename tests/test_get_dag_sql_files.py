import pytest
from dags.python_files.lib.sql_folder import get_dag_sql_files

def get_dag_sql_files(dag_folder: str = None ,
                        dag_sub_folder: str = None):
    
    """
    Agarra todos los archivos sql dentro de una carpeta, por default la del mismo nombre del dag.
    Opcional tambien ponerle una subcarpte
    :param dag_folder: carpeta donde estan los sql de ese DAG -> por default es el nombre del dag
    :dag_sub_folder: subcarpeta dentro de la anterior - opcional
    """

def test_get_dag_sql_files_without_sub_folder():
    dag_folder = 'l2'
    expected_path = 'dags/sql_files/l2'
    result = get_dag_sql_files(dag_folder=dag_folder)
    print(result)
    assert result == expected_path
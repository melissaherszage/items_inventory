import pytest

def get_dag_sql_files(dag_folder: str = None ,
                        dag_sub_folder: str = None):
    
    """
    Agarra todos los archivos sql dentro de una carpeta, por default la del mismo nombre del dag.
    Opcional tambien ponerle una subcarpte
    :param dag_folder: carpeta donde estan los sql de ese DAG -> por default es el nombre del dag
    :dag_sub_folder: subcarpeta dentro de la anterior - opcional
    """

    #  Defino el path de la carpeta donde voy a buscar los archivos
    if dag_sub_folder is not None:
        path = f'dags/sql_files/{dag_folder}/{dag_sub_folder}'
    else:
        path = f'dags/sql_files/{dag_folder}' 
    return path

def test_get_dag_sql_files_without_sub_folder():
    dag_folder = 'l2'
    expected_path = 'dags/sql_files/l2'
    result = get_dag_sql_files(dag_folder=dag_folder)
    print(result)
    assert result == expected_path



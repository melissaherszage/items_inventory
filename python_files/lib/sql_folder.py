import os

def get_dag_sql_files(dag_folder: str = None ,
                        dag_sub_folder: str = None):
    
    """
    Agarra todos los archivos sql dentro de una carpeta,
    Opcional tambien ponerle una subcarpeta
    :param dag_folder: carpeta donde estan los sql de ese DAG -> por default es el nombre del dag
    :dag_sub_folder: subcarpeta dentro de la anterior - opcional
    """
    if dag_sub_folder is not None:
        path = f'dags/sql_files/{dag_folder}/{dag_sub_folder}'
    else:
        path = f'dags/sql_files/{dag_folder}' 
    
    print(f"Searching in path: {path}")

    sql_files = [f for f in os.listdir(path) if f.endswith('.sql')]
    print(f"SQL files found: {sql_files}")
    
    #full_paths = [os.path.join(path, f) for f in sql_files]
    
    #return full_paths

    relative_paths = [f"sql_files/{dag_folder}/{dag_sub_folder}/{f}" if dag_sub_folder else f"sql_files/{dag_folder}/{f}" for f in sql_files]
    
    return relative_paths

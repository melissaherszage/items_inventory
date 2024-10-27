import os

def get_dag_sql_files(dag_folder: str = None,
                        dag_sub_folder: str = None):
    
    """
    Obtiene los archivos SQL dentro de una carpeta específica para un DAG.
    
    Args:
        dag_folder (str): Carpeta donde están los SQL de ese DAG. Por defecto, es el nombre del DAG.
        dag_sub_folder (str, optional): Subcarpeta dentro de 'dag_folder', opcional.
        
    Returns:
        list: Lista de rutas relativas de los archivos SQL encontrados en la carpeta especificada.
        
    Raises:
        FileNotFoundError: Si la carpeta especificada no existe.
    """

    if dag_sub_folder is not None:
        path = f'dags/sql_files/{dag_folder}/{dag_sub_folder}'
    else:
        path = f'dags/sql_files/{dag_folder}' 
    
    print(f"Searching in path: {path}")

    sql_files = [f for f in os.listdir(path) if f.endswith('.sql')]
    print(f"SQL files found: {sql_files}")
    
    relative_paths = [f"sql_files/{dag_folder}/{dag_sub_folder}/{f}" if dag_sub_folder else f"sql_files/{dag_folder}/{f}" for f in sql_files]
    
    return relative_paths
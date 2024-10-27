import os

def get_dag_id(file_path):
    """Obtiene el ID del DAG basado en el nombre de archivo"""
    return os.path.basename(file_path).replace(".py", "")

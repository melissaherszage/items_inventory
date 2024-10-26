import pytest
import os
from python_files.lib.sql_folder import get_dag_sql_files

def test_get_dag_sql_files_without_sub_folder():
    dag_folder = 'l2'
    expected_path = 'sql_files/l2'
    result = get_dag_sql_files(dag_folder=dag_folder)
    print(result)
    assert all(file.startswith(expected_path) for file in result), f"Resulting files do not start with {expected_path}"

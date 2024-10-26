import os
import pytest
from python_files.lib.get_dag_id import get_dag_id

def test_dag_id(monkeypatch):
    monkeypatch.setattr(os.path, 'basename', lambda _: 'nombre_del_dag.py')

    dag_id = get_dag_id(__file__)

    assert dag_id == "nombre_del_dag"
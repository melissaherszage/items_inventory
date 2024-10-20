import os
import pytest

def test_dag_id(monkeypatch):
    monkeypatch.setattr(os.path, 'basename', lambda _: 'nombre_del_dag.py')

    dag_id = os.path.basename(__file__).replace(".py", "")

    assert dag_id == "nombre_del_dag"
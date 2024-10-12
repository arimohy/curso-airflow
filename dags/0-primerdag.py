from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.empty import EmptyOperator


with DAG(dag_id="primerdag",
         description="Nuestro preimer dag",
         start_date=datetime(2022,7,1),
         schedule_interval="@once") as dag:
    
    t1=EmptyOperator(task_id="dummy")
    t1
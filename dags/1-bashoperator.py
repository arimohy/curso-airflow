from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(dag_id="bashoperator",
         description="Utilizando bah operator",
         start_date=datetime(2022,8,1)) as dag:
    
    t1=BashOperator(task_id="hello_eith_bash",
                    bash_command="echo 'Hello gente'")
    t1


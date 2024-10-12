from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

def myfuncion():
    pass

with DAG(dag_id="6.1-monitoring",
         description="Monitoriando nuestro DAG",
         schedule_interval="@daily",
         start_date=datetime(2022,1,1),
         end_date=datetime(2022,2,1)) as dag:  
    
    t1 =BashOperator(task_id="tarea1",
                     bash_command="sleep 2 && echo 'Tarea 1 '")
    
    t2 =BashOperator(task_id="tarea2",
                     bash_command="sleep 2 && echo 'Tarea 2'")
    
    t3 =BashOperator(task_id="tarea3",
                     bash_command="sleep 2 && echo 'Tarea 3'")
    t4 =PythonOperator(task_id="tarea4",
                       python_callable=myfuncion)
    
    t5 =BashOperator(task_id="tarea5",
                     bash_command="sleep 2 && echo 'Tarea 5'")
    
    t1 >> t2 >> t3 >> t4 >>t5
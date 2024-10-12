from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(dag_id="5.1-orquestacion",
         description="Probando orquestacion",
         schedule_interval="@daily",
         start_date=datetime(2022,1,1),
         end_date=datetime(2022,6,1),
         default_args={"depends_on_past":True},#linea hace que dependa y se ejecute mas dependencia
         max_active_runs=1) as dag:  #espera a que todas las tareas terminen para iniciar otro
    
    t1 =BashOperator(task_id="tarea1",
                     bash_command="sleep 2 && echo 'Tarea 1'")
    
    t2 =BashOperator(task_id="tarea2",
                     bash_command="sleep 2 && echo 'Tarea 2'")
    
    t3 =BashOperator(task_id="tarea3",
                     bash_command="sleep 2 && echo 'Tarea 3'")
    
    t4 =BashOperator(task_id="tarea4",
                     bash_command="sleep 2 && echo 'Tarea 4'")
    
    t1 >> t2 >> [t3,t4]
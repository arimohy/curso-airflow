from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.email  import EmailOperator
from datetime import datetime

def _generate_platzi_data(**kwargs):
    import pandas as pd
    data = pd.DataFrame({
        "student": ["Maria Cruz", "Daniel Crema", "Elon Musk", "Karol Castrejon", "Freddy Vega"],
        "timestamp": [kwargs['logical_date']] * 5
    })
    data.to_csv(f"/tmp/platzi_data_{kwargs['ds_nodash']}.csv", header=True)

with DAG(
    dag_id="ProyectoExploraElEspacio",
    description="DAG proyecto",
    schedule_interval="@daily",
    start_date=datetime(2022, 8, 10),
    end_date=datetime(2022, 8, 25)
) as dag:

    t1 = BashOperator(
        task_id="Autorizacion_Nasa",
        bash_command="sleep 20 && echo 'Se autoriza' >/tmp/response_{{ds_nodash}}.txt"
    )
    
    t2 = BashOperator(
        task_id="LeerDatosNasa",
        bash_command='ls /tmp && head /tmp/response_{{ds_nodash}}.txt'
    )

    t3 = BashOperator(
        task_id="ObtencionSpaceX",
        bash_command="curl -o /tmp/history.json -L 'https://api.spacexdata.com/v4/history'"
    )
    
    t4 = PythonOperator(
        task_id="generardata",
        python_callable=_generate_platzi_data
    )

    send_email = EmailOperator(
        task_id='send_email',
        to='arimohy@gmail.com',
        subject='espacio informacion',
        html_content="Date: {{ ds }}"
    )
    
    t1 >> t2 >> t3 >> t4 >> send_email

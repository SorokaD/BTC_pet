from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def print_hello():
    print(f'Running time {datetime.now()}')
    return 'Hello world from first Airflow DAG from Soroka!'

dag = DAG('hello_world', description='Hello World DAG',
          schedule_interval='30 0 * * *',
          tags=['soroka', 'time'],
          start_date=datetime(2024, 1, 15), catchup=False)

hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

hello_operator 
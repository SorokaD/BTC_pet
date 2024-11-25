from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook
from airflow.hooks.base_hook import BaseHook


# Working scheme !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def print_hello():
    print('print1 Soroka!!!!!!!!!!!!!!!!!!!!!!!!!!')

    postgres = PostgresHook(postgres_conn_id='postgres_connection')
    '''conn = postgres.get_conn()
    cursor = conn.cursor()
    sql = 'SELECT * FROM data.currency'
    cursor.execute(sql)
    print(cursor)'''
    print(postgres)
    
    conn = BaseHook.get_connection('postgres_connection')
    conn = postgres.get_conn()
    cursor = conn.cursor()
    sql = 'SELECT * FROM data.symbols'
    cursor.execute(sql)
    print(cursor.fetchall())
 
    print('print2 Soroka!!!!!!!!!!!!!!!!!!!!!!!!!!')
    return 'success'
    

dag = DAG('dag_postgres', description='Hello World DAG',
          schedule_interval='30 0 * * *',
          tags=['soroka'],
          start_date=datetime(2024, 1, 15), catchup=False)

hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

hello_operator 
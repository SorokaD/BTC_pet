from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook
from airflow.hooks.base_hook import BaseHook
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from pybit.unified_trading import HTTP

from credentials import KEY_test, SECRET_test, DB_username, DB_password, DB_host, DB_name

import src_API

# create Bybit client 
client = HTTP(testnet=True, api_key=KEY_test, api_secret=SECRET_test)

# connect to BD with PostgresHook for read
postgres = PostgresHook(postgres_conn_id='postgres_connection')
conn = BaseHook.get_connection('postgres_connection')
conn = postgres.get_conn()
cursor = conn.cursor()

# create engine with sqlalchemy for write
for_engine = f'postgresql+psycopg2://{DB_username}:{DB_password}@host.docker.internal:5432/{DB_name}'
engine = create_engine(for_engine)

# global var
category = {'spot':1, 'linear':2}
category = {'linear':2}
interval = {1:1, 3:2, 5:3, 15:4, 30:5, 60:6, 120:7, 240:8, 360:9, 720:10, 'D':11}
equal_dict = {1: 60000,
              3: 180000,
              5: 300000,
              15: 900000, 
              30: 1800000,
              60: 3600000,
              120: 7200000,
              240: 14400000,
              360: 21600000,
              720: 43200000,
              'D': 86400000}
symbol_dct = {'BTCUSDT': 1, 'ETHUSDT':2}
symbol = 'ETHUSDT'
limit = 1000
source = 3

# get end/current time
end = src_API.convert_dt_to_timestamp( str( pd.to_datetime(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) ) )

# DAG definition
dag = DAG(f'ETL_kline_mark_price_{symbol}',
    schedule_interval='55 0 * * *',
    start_date = datetime(2024,3,11),
    catchup=False,
    tags=['ETL','soroka']
    )

def extract_transform(ti):
    '''
    Extract & transform function 
    '''
    data_extracted = pd.DataFrame()
    for i in list(category.keys()):
        for j in list(interval.keys()):
            # finding current max date in BD 
            query = text("SELECT max(datetime) mdt FROM data.kline_mark_price where category=:category and symbol=:symbol and interval=:interval")
            date_max = pd.read_sql(query, con=engine, params={'category': category.get(i), 'symbol': symbol_dct.get(symbol), 'interval': interval.get(j)})
            print(i, category.get(i), j, interval.get(j), date_max)
            current = src_API.convert_dt_to_timestamp( str(date_max.loc[0,'mdt']) )  + equal_dict.get(j)
            lag = current + equal_dict.get(j)*(limit)
            while current <= end:
                lag = current + equal_dict.get(j)*(limit)
                data = src_API.get_mark_price_kline(client, i, symbol, j, start=current, limit=limit)
                data.dropna(inplace=True)
                current = lag
                if data.shape[0] == 0:
                    continue
                data['category'] = category.get(i)
                data['interval'] = interval.get(j)
                data['symbol'] = symbol_dct.get(symbol)
                data['source'] = source
                data['created_dt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
                #display(data)
                data_extracted = pd.concat([data_extracted, data[['datetime', 'category', 'interval', 
                    'symbol', 'open', 'high', 'low', 
                    'close', 'source', 'created_dt']] ], axis=0)
    ti.xcom_push(key='data', value=data_extracted)
    return True

def load(ti):
    '''
    Load function to BD
    '''
    data = ti.xcom_pull(key='data')
    data.to_sql(name='kline_mark_price', schema='data', con=engine, if_exists='append', index=False)
    return True


extract_transform = PythonOperator(task_id='extract_transform', python_callable=extract_transform, dag=dag)
load = PythonOperator(task_id='load', python_callable=load, dag=dag)

extract_transform >> load
# по материалам:
# https://alimbekov.com/machine-learning-flask-rest-api/
# на вход подаем customer_id в ответ получаем данные о клиенте

import os
from flask import Flask, jsonify, abort, make_response, request
import requests
import json
import time
import sys
import pandas as pd
from typing import Dict, List
from sqlalchemy import create_engine, Integer, Column
#from sqlalchemy.ext.declarative import declarative_base # старая схема
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker, declarative_base
from psycopg2 import connect
import random

# подтягиваем модуль с "моделью"
import model as M

# логирование
import logging
# указываем путь к файлу с логами
logging.basicConfig(filename='logs/logs.log',level=logging.DEBUG)

# прописываем параметры базы
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=

db_url = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# вся байда отсюда:
# https://davidcaron.dev/sqlalchemy-multiple-threads-and-processes/ 
engine = create_engine(
    db_url,
    pool_size=5,     # default in SQLAlchemy
    max_overflow=10, # default in SQLAlchemy
    pool_timeout=1  # raise an error faster than default
)
Session = sessionmaker(bind=engine)
Base = declarative_base()


# байда не понятная
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

Base.metadata.create_all(engine)

def get_connections() -> List[Dict]:
    """Return information about connections"""
    sql = """
    SELECT
        pid,
        state
    FROM pg_stat_activity
    WHERE datname = 'postgres'
    AND query NOT LIKE '%%FROM pg_stat_activity%%'
    """
    connection = connect(db_url)
    cursor = connection.cursor()
    cursor.execute(sql)
    connections = [
        {"pid": r[0], "state": r[1]} for r in cursor.fetchall()
    ]
    cursor.close()
    connection.close()
    return connections

# Функция олбработки SQL запроса 
def get_sql_query(id) -> List[Dict]:
    """Return result of sql query"""
    sql = text("SELECT id, customer_id, customername FROM dbo.customers WHERE id = :id")
    with engine.connect() as conn:
        result = conn.execute(sql, {'id':id})
    result = pd.DataFrame(result)
    print('result', result)
    #cursor.close()
    conn.close()
    return {'result':  json.loads( pd.DataFrame(result).to_json(orient='records'))}


def get_pool_info() -> Dict:
    """Get information about the current connections and pool"""
    return {
        "postgres connections": get_connections(),
        "pool id": id(engine.pool),
        "connections in current pool": (
            engine.pool.checkedin() + engine.pool.checkedout()
        ),
    }


app = Flask(__name__)

# Create a session and make a query.
# The connection created is now part of the pool.
session = Session()
session.query(User).all()
session.close()


@app.route("/pool")
def pool():
    return jsonify(get_pool_info())


@app.route("/make_query")
def make_query():
    session = Session()
    session.query(User).all()
    session.close()
    return jsonify(get_pool_info())


@app.route("/dispose")
def dispose():
    engine.pool.dispose()
    return jsonify(get_pool_info())


@app.route('/query', methods=['GET']) # GET
# get_task использует метод GET и на вход получает необходимые для работы модели признаки
def get_task():
    result = get_sql_query(request.args.get('id'))
    return jsonify(result)


# запуск по адресу хоста
if __name__ == '__main__':
    # 0.0.0.0:80 - 80-ый порт локальной машины docker контейнера, прописывается обязательно!!! затем указывается в "docker run ..."
    app.run(host='0.0.0.0', port=80, debug=True) # ИМЕННО рабочий вариант для работы из docker контейнера!!!
    # host='172.17.0.2' - берется из информации о запуске контейнера, port=80 - задается 
    #app.run(host='localhost', port=5070, debug=True) # рабочий вариант для работы на локальной машине !!!
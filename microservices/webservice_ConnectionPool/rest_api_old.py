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
#from sqlalchemy.ext.declarative import declarative_base
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
DB_NAME='kompaniondwh' #база dwh
DB_USER='dsoroka'  #имя пользователя dwh
DB_PASSWORD='YIJyuiHlw'   #пароль пользователя dwh
DB_HOST='dwh-db-test.test'   #host dwh

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

# запуск по адресу хоста
if __name__ == '__main__':
    app.run(host='172.17.0.2', port=5000, debug=True) # рабочий вариант !!!
    #app.run(host='localhost', port=5000, debug=True) # не рабочий вариант ?


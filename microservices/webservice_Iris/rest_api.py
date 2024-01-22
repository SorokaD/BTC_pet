# по материалам:
# https://alimbekov.com/machine-learning-flask-rest-api/

import os
from flask import Flask, jsonify, abort, make_response, request
import requests
import json
import time
import sys
import pandas as pd

# подтягиваем модуль с "моделью"
import model as M

# логирование
import logging
# указываем путь к файлу с логами
logging.basicConfig(filename='logs/logs.log',level=logging.DEBUG)

# создаем экземпляр класса flask
app = Flask(__name__)

# получаем нашу модель (случаное число)
model = M.randomer() 

# get_pred получает на входе значения и возвращает список из двух фреймов 
# первое значение списка - результат "работы модели" 
# второе значение списка - входные данные 
def get_pred(sepal_length, sepal_width, petal_length, petal_width):
    
    all_columns = ['sepal length', 'sepal width', 'petal length', 'petal width']
    lst = [sepal_length, sepal_width, petal_length, petal_width]
    df = pd.DataFrame([lst], columns = all_columns)
    
    df = df.astype(float)
    # "предсказание" = входные данные умножить на случайное число
    result = df*model
    return [result, df]

def launch_task(sepal_length, sepal_width, petal_length, petal_width, api):

    pred_model = get_pred(sepal_length, sepal_width, petal_length, petal_width)[0]
    basic_data = get_pred(sepal_length, sepal_width, petal_length, petal_width)[1]
    
    logging.debug('Ошибка')
    logging.info('Информационное сообщение')
    logging.warning('Предупреждение')

    if api == 'v1.0':
        res_dict = {'result':  json.loads( pd.DataFrame(pred_model).to_json(orient='records'))}
        bas_dat = {'result':  json.loads( pd.DataFrame(basic_data).to_json(orient='records'))}
        return res_dict, bas_dat
    else:
        res_dict = {'error': 'API doesnt exist'}
        return res_dict

@app.route('/iris/api/v1.0/getpred', methods=['GET']) # GET
# get_task использует метод GET и на вход получает необходимые для работы модели признаки
# последовательностью '/iris/api/v1.0/getpred' задается имя запроса !!!
def get_task():
    result = launch_task(request.args.get('sepal_length'), request.args.get('sepal_width'), \
                        request.args.get('petal_length'), request.args.get('petal_width'), 'v1.0')
	
    return make_response(jsonify(result), 200)

# обработка ошибок !!
# проверяется неверным запросом по верному адресу

# 404 — «Не найдено» # 500 — «внутренняя ошибка сервера»
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'code': 'soroka_PAGE_NOT_FOUND'}), 404)

# 500 — «внутренняя ошибка сервера»
@app.errorhandler(500)
def server_error(error):
    return make_response(jsonify({'code': 'soroka_INTERNAL_SERVER_ERROR'}), 500)

# запуск по адресу хоста
if __name__ == '__main__':
    app.run(host='172.17.0.2', port=5000, debug=True) # рабочий вариант для работы из docker контейнера!!!
    # host='172.17.0.2' - берется из информации о запуске контейнера, port=5000 - задается 
    #pp.run(host='localhost', port=5000, debug=True) # рабочий вариант для работы на локальной машине из коммандной строки!!!

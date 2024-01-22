import logging
import traceback
from time import time

from flask import request, Response, g

from configuration import LOGGER_NAME, BACKUP_COUNT
from script import get_score
from utils import json_response, create_application

application = create_application(name=__name__, logger_name=LOGGER_NAME, backup_count=BACKUP_COUNT)


@application.before_request
def before():
    logging.info(u'{0}: Request:{1} - Data:{2}'.format(request.remote_addr, request.url, request.json))


@application.after_request
def after(response):
    logging.info('Response data: {0}'.format(response.json))
    return response


@application.teardown_request
def teardown(exception):
    if not hasattr(g, 'time'):
        g.time = time()
    logging.info('{0}: Request: {1} finished in {2} sec'.format(request.remote_addr, request.url, time() - g.time))


@application.errorhandler(Exception)
def core_error(e):
    code = ''
    if hasattr(e, 'code'):
        code = str(e.code)
    logging.error(traceback.format_exc() + code)


@application.route("/scoring", methods=['POST'])
def scoring():
    data = request.json
    result = get_score(data)
    if isinstance(result, Response):
        return result
    return json_response(result)


@application.route("/health", methods=['GET'])
def health():
    return json_response({'status': 'Service is fine'})


if __name__ == "__main__":
    application.run(host="localhost", port=5050)

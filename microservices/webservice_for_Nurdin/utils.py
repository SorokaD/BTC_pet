import datetime
import decimal
import json
import logging

from logging.handlers import TimedRotatingFileHandler

from flask import Response, Flask

from configuration import LOG_LEVEL, LOGGER_PATH


class JSONEncoderLocal(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return str(o)[:19]
        if isinstance(o, datetime.date):
            return str(o)
        if isinstance(o, datetime.time):
            return str(o)
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(JSONEncoderLocal, self).default(o)


def create_application(name, logger_name, backup_count):
    logging.basicConfig(level=LOG_LEVEL, format="%(threadName)s %(asctime)s %(name)-12s %(message)s",
                        datefmt="%d-%m-%y %H:%M")
    daily = logging.handlers.TimedRotatingFileHandler(filename=LOGGER_PATH + "/" + logger_name, when="midnight",
                                                      interval=1, backupCount=backup_count, encoding="utf-8")
    logging.getLogger().addHandler(daily)
    fmt = logging.Formatter('%(asctime)s %(name)-12s %(message)s')
    daily.setFormatter(fmt)
    app = Flask(name)
    return app


def json_response(context):
    json_string = json.dumps(context, cls=JSONEncoderLocal)
    result = Response(json_string, mimetype='application/json; charset=utf-8')
    return result

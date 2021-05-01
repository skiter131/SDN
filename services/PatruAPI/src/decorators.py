"""
this is archive .py
declare the decorators
"""

import logging
import functools
import graypy
from src.core.parameters import CORS
import traceback

class EventidFilter(logging.Filter):
    def __init__(self, id):
        """
        In an actual use case would dynamically get this
        (e.g. from memcache)
        """
        self.id = id

    def filter(self, record):
        record.eventid = self.id
        return True

class ServiceFilter(logging.Filter):
    def __init__(self):
        """
        In an actual use case would dynamically get this
        (e.g. from memcache)
        """
        self.service = 'features_service'

    def filter(self, record):
        record.service = self.service
        return True


def create_log(function):
    """
    Create archive log
    Args: function
    Return: the function.
    """

    def wrapper(*args, **kwargs):

        logger = logging.getLogger()
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)

        logger.setLevel(logging.DEBUG)
        handler = graypy.GELFUDPHandler('graylog', 12201, debugging_fields=False)
        logger.addHandler(handler)
        logger.addFilter(ServiceFilter())

        try:
            eventid = args[0].get_json()['eventid']
        except:
            eventid = 'nao identificado'

        logger.addFilter(EventidFilter(eventid))

        return function(*args, **kwargs)

    return wrapper


def validate_request(function):
    """
    Creates a logging object and returns it
    """

    def wrapper(*args, **kwargs):

        # Valida consistência da request
        json_body = args[0].get_json()

        if json_body is None:
            logging.error('Json body não encontrado na requisição')
            return 'json body is not found', 404, CORS

        if 'cli' not in json_body or not json_body['cli']:
            logging.error(f'Identificação de evento não encontrada (cli key)')
            return 'eventid key was not found', 404, CORS

        logging.info(f'Requisição do evento - {json_body["eventid"]} aceita')

        # Check token
        authorization = args[0].headers.get('authorization', '')
        if authorization != '12mioearfmaroakm2121@#i':
            logging.error('Autorização não encontrada/permitida.')
            return 'Missing authorization', 401, CORS

        logging.info('Dados de requisição corretos')
        logging.info(f'Requisição recebida de {args[0].path}')

        return function(*args, **kwargs)

    return wrapper


def exception(function):
    """
    A decorator that wraps the passed in function and logs
    exceptions should one occur
    """

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as ex:
            # log the exception
            traceback.print_exc()
            logging.exception('Erro inesperado')
            return 'Ocorreu um erro inesperado', 500, CORS

    return wrapper
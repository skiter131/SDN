"""
Este arquivo .py gera os dados
a serem computados e analisados em nossa
aplicação
"""

import json
import logging
import numpy as np
import pandas as pd
from src.decorators import exception
from src.core.parameters import CORS
import requests

@exception
def request_api(req):

    """
    Função que configura a api

    :Args: req flask dependencia

    :Retorna: JSON com os dados
    """

    if req.method == 'POST':

        json_body = req.get_json()
        IP_ADRESS = json_body['cli_commands']

        request_data = {
            "username": "developer",
            "password": "C1sco12345"
        }

        req = requests.post(f'https://{IP_ADRESS}/api/v0/authenticate', headers={'authorization':\
        '2j3k3o5p5i3p1p3oi', 'Content-Type': 'application/json',},\
            data=json.dumps(request_data))

        return req.text, 201, CORS
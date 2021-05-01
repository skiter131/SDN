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
import cli

@exception
def request_api(req):

    """
    Função que configura a api

    :Args: req flask dependencia

    :Retorna: JSON com os dados
    """

    if req.method == 'POST':

        json_body = req.get_json()
        cli_commands = json_body['cli_commands']
        cli.cli(cli_commands)

        return cli_commands, 201, CORS
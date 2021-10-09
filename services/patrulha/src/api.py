"""
Este arquivo .py gera os dados
a serem computados e analisados em nossa
aplicação
"""

# import json
# import logging
# import numpy as np
# import pandas as pd
# import requests
from src.decorators import exception
from src.core.parameters import CORS
from netmiko import ConnectHandler


@exception
def request_api(req):

    """
    Função que configura a api

    :Args: req flask dependencia

    :Retorna: JSON com os dados
    """

    if req.method == 'POST':

        json_body = req.get_json()

        #Informações do Usuario
        cisco = { 
            'device_type': json_body['device'], 
            'host': 'sandbox-iosxe-latest-1.cisco.com', 
            'username': 'developer', 
            'password': 'C1sco12345'
        }  

        # 'cisco_ios'

        #Conexão com o elemento
        net_connect = ConnectHandler(**cisco)
        net_connect.find_prompt()

        #Comando Enviado
        output = net_connect.send_command("show runn")

        #Saida do comando
        #print(output)

        return output, 201, CORS
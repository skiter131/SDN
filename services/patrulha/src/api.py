"""
Este arquivo .py gera os dados
a serem computados e analisados em nossa
aplicação
"""

# import pandas as pd
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
            'host': json_body['host'], 
            'username': json_body['user'], 
            'password': json_body['pass']
        }

        # 'cisco_ios'

        #Conexão com o elemento
        net_connect = ConnectHandler(**cisco)
        net_connect.find_prompt()

        config_commands = json_body['commands']

        output = net_connect.send_config_set(config_commands)

        #Comando Enviado no list
        #output = net_connect.send_command(json_body['command'])

        #Saida do comando
        #print(output)

        return output, 201, CORS
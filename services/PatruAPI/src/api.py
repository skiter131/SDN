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
from netmiko import ConnectHandler
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
        command_body = json_body['cmd']
       
        cisco = { 
            'device_type': 'cisco_ios', 
            'host': 'sandbox-iosxe-latest-1.cisco.com', 
            'username': 'developer', 
            'password': 'C1sco12345', 
        }  

        net_connect = ConnectHandler(**cisco)
        net_connect.find_prompt()

        #config_commands = ['do show int g1', 'do show ip int brief']

        output =  net_connect.send_config_set(command_body)
        
        return output, 201, CORS
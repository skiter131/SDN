from src.decorators import exception, validate_request
from src.core.parameters import CORS
from netmiko import ConnectHandler

@validate_request
@exception
def request_api(req):

    """
    Função que configura a api

    :Args: req flask dependencia

    :Retorna: JSON com os dados
    """

    if req.method == 'POST':

        json_body = req.get_json()

        # 'cisco_ios'
        cisco = { 
            'device_type': 'cisco_ios', 
            'host': json_body['host'], 
            'username': 'patrulha', 
            'password': '1234',
            'secret' :  'patrulha123'
        }

        #commands = "show ip int brief"

        with ConnectHandler(**cisco) as net_connect:
            net_connect.enable()
            output = net_connect.send_config_set(json_body['commands'])

        return output, 201, CORS
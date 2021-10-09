"""
Serviços para gerar o endpoint da aplicação
"""

import src.api as request_api
from src.core.parameters import CORS
from src.decorators import validate_request, exception

@validate_request
@exception
def services(req):
    """
    Nome:
        Services
    
    Descrição:
        Função de requisição dos endpoints

    :Args: requisição flask

    :Retorna: endpoints com determinado valor pedido na requisição
    """

    print("received request for", req.path)
    return request_api.request_api(req) if req.path.startswith("/apipatrulha") \
        else ("Service not available", 404, CORS)

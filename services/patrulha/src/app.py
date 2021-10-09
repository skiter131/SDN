"""
Servidor para rodar o docker com o flask
"""

from flask import Flask, request
from flask_swagger_ui import get_swaggerui_blueprint
from src.main import services

APP = Flask(__name__)

## Swagger ##
SWAGGER_URL = '/apipatrulha/docs'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Patrulha API"
    }
)
APP.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
## End Swagger ##

@APP.route("/<path:path>", methods=['GET', 'POST'])
def service(path):
    """
    Name: Service

    Descrição:
        Retorna o enpoint requisitado

    Args: path (endpoint)

    Return: request /path
    """
    return services(request)

if __name__ == "__main__":
    APP.run(host="0.0.0.0", debug=True)

"""
Arquivo de testes 

==================

Para rodar os testes basta
entrar na pasta tests
e make test

"""

import unittest
import json
from pytest import mark 
from pathlib import Path
from src.app import APP, SWAGGER_URL
from src.decorators import validate_request, create_log

@mark.describe("Teste da API")
class Test_Features(unittest.TestCase):
    """
    Testes para o microserviço de features
    """

    def setUp(self):
        """
        Nome: setUp

        Descrição: 
            Define as variaveis do ambiente 
        
        Args: self
        """

        data_folder = Path("archives/features.json")
        file = open(data_folder)
        json_data = json.load(file)

        self.app = APP
        self.application = self.app.test_client()
        self.app.testing = True
        self.headers = {'Authorization': '2j3k3o5p5i3p1p3oi', 'Content-Type': 'application/json'}
        self.response = self.application.post('/features', json=json_data, headers=dict(self.headers))
        APP.config['TESTING'] = True

    @mark.it("Testa se o modo debug está desativado")
    def test_debug_is_false(self):
        """
        Testa se o modo DEBUG de Dev está desativado
        """
        assert APP.config['DEBUG'] is False

    @mark.it("Testa se ENV Está no modo de produção")
    def test_env_is_production(self):
        """
        testa se env está em produção
        """
        assert APP.config['ENV'] is 'production'

    @mark.it("Testa se o APP não foi modificado o nome")
    def test_app_name(self):
        """
        Testa se houve alguma modificação no nome
        do app do Flask
        """
        assert APP.name == 'src.app'

    @mark.it("Testa se a URL do swagger não foi modificada")
    def test_swagger_url(self):
        """
        Nome: Testa se a URL do swagger não foi modificada

        Descrição: 
            Observa se a URL do swagger não foi modificada após 
            alguma modificação.

        Args: self
        """
        assert SWAGGER_URL == '/features/docs'

    @mark.it("Testa se com um body correto a API retorna o código 201")
    def test_post_with_body_return_201(self):
        """
        Nome: Teste com um body na requisição

        Descrição: 
            Gera uma requisição HTTP, coleta
            o status code do servidor
            e testa se retorna 201

        Args: self
        """
        self.assertEqual(201, self.response.status_code)

    @mark.it("Testa se sem um json body no request a API retorna um erro 404")
    def test_post_without_body(self):
        """
        Nome: Teste sem um body na requisição

        Descrição:
            Gera uma requisição HTTP sem um body
            esse teste deve retornar um erro 400

        Args: self
        """

        self.headers = {'Authorization': '2j3k3o5p5i3p1p3oi'}
        self.response = self.application.post('/features', headers=dict(self.headers))
        self.assertEqual(404, self.response.status_code)

    @mark.it("Testa se a resposta se adequa com o que foi imposto como regra do código")
    def test_json_string_response(self):
        """
        Nome:Teste retorno string json 

        Descrição:
            Testa se o retorno da função
            é um json como pedido na 
            requisição

        Args :self
        """
        data_folder = Path("archives/response.json")
        file = open(data_folder)
        response_expected = json.load(file)

        json_response = json.loads(self.response.data.decode())
        self.assertEqual(response_expected, json_response)

    @mark.it("Testa se o content type é text/html")
    def test_content_type(self):
        """
        Nome: test content type

        Descrição: 
            Testa se os valores retornados
            estão de acordo com o pedido
            no request

        Args: self
        """
        self.assertIn('text/html', self.response.content_type)

    @mark.it("Testa se o valor da autorização está correto")
    def test_authorization_value(self):
        """
        Nome: test authorization

        Descrição:
            Testa se o valor da autorização 
            está de acordo com o programado 
            no request

        Args: self
        """
        self.assertEqual('2j3k3o5p5i3p1p3oi', self.headers['Authorization'])

    @mark.it("Testa se o request a API funciona sem a autorização")
    def test_authorization_empty_value(self):
        """
        Nome: test authorization empty

        Descrição:
            Testa se sem o valor da autorização 
            o microserviço aponta para 
            o status code 401 UNAUTHORIZED

        Args: self
        """

        data_folder = Path("archives/features.json")
        file = open(data_folder)
        json_data = json.load(file)

        self.headers = {}
        self.response = self.application.post('/features', json=json_data, headers=dict(self.headers))
        self.assertEqual(401, self.response.status_code)

    @mark.it("Testa se a API aceita um tipo diferente de autorização")
    def test_authorization_different_value(self):
        """
        Nome: test authorization empty

        Descrição:
            Testa se sem o valor da autorização 
            o microserviço aponta para 
            o status code 401 UNAUTHORIZED

        Args: self
        """

        data_folder = Path("archives/features.json")
        file = open(data_folder)
        json_data = json.load(file)

        self.headers = {'Authorization': '123', 'Content-Type': 'application/json'}
        self.response = self.application.post('/features', json=json_data, headers=dict(self.headers))
        self.assertEqual(401, self.response.status_code)

    @mark.it("Testa se sem a chave eventid no json body a API retorna um erro 404")
    def test_no_content_eventid_json_body(self):
        """
        Nome: test no content eventid in json body

        Descrição:
            Testa se não existe o valor
            eventid no json_body

        Args: self
        """

        data_folder = Path("archives/features_no_eventid.json")
        file = open(data_folder)
        json_data = json.load(file)

        self.headers = {'Authorization': '2j3k3o5p5i3p1p3oi',  'Content-Type': 'application/json'}
        self.response = self.application.post('/features', json=json_data, headers=dict(self.headers))

        self.assertEqual(404, self.response.status_code)

    @mark.it("Testa se sem a chave df no json body a API retorna um erro 404")
    def test_no_content_df_json_body(self):
        """
        Nome: test no content df in json body

        Descrição: 
            Testa se não existe o valor
            df no json_body

        Args: self
        """

        data_folder = Path("archives/features_no_df.json")
        file = open(data_folder)
        json_data = json.load(file)

        self.headers = {'Authorization': '2j3k3o5p5i3p1p3oi',  'Content-Type': 'application/json'}
        self.response = self.application.post('/features', json=json_data, headers=dict(self.headers))

        self.assertEqual(404, self.response.status_code)  
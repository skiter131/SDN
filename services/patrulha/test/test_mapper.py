"""
Arquivo de testes 

==================

Para rodar os testes basta
entrar na pasta /tests
e rodar py.test --cov=src

"""
import unittest
import json
from pathlib import Path
from src.app import app

class Test_Mapper(unittest.TestCase):
    """
    Testes para o microserviço de mapper
    """

    def setUp(self):
        """
        Nome: setUp

        Descrição: 
            Define as variaveis do ambiente 
        
        Args: self

        """

        data_folder = Path("archives/mapper.json")
        file = open(data_folder)
        json_data = json.load(file)

        self.app = app
        self.application = self.app.test_client()
        self.app.testing = True
        self.headers = {'Authorization': '2j3k3o5p5i3p1p3oi', 'Content-Type': 'application/json'}
        self.response = self.application.post('/mapper', json=json_data, headers=dict(self.headers))

    def test_debug_is_false(self):
        """
        Testa se o modo DEBUG de Dev está desativado
        """

        assert app.config['DEBUG'] is False

    def test_env_is_production(self):
        """
        testa se env está em produção
        """
        assert app.config['ENV'] is 'production'

    def test_app_name(self):
        """
        Testa se houve alguma modificação no nome
        do app do Flask
        """
        assert app.name == 'src.app'

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

    def test_post_without_body(self):
        """
        Nome: Teste sem um body na requisição

        Descrição:
            Gera uma requisição HTTP sem um body
            esse teste deve retornar um erro 404

        Args: self
        """

        self.headers = {'Authorization': '2j3k3o5p5i3p1p3oi'}
        self.response = self.application.post('/mapper', headers=dict(self.headers))
        self.assertEqual(404, self.response.status_code)


    def test_json_string_response(self):
        """
        Nome:Teste string json 

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
    
    def test_authorization_empty_value(self):
        """
        Nome: test authorization empty

        Descrição:
            Testa se sem o valor da autorização 
            o microserviço aponta para 
            o status code 401 UNAUTHORIZED

        Args: self
        """

        data_folder = Path("archives/mapper.json")
        file = open(data_folder)
        json_data = json.load(file)

        self.headers = {}
        self.response = self.application.post('/mapper', json=json_data, headers=dict(self.headers))
        self.assertEqual(401, self.response.status_code)

    
    def test_authorization_different_value(self):
        """
        Nome: test authorization empty

        Descrição:
            Testa se sem o valor da autorização 
            o microserviço aponta para 
            o status code 401 UNAUTHORIZED

        Args: self
        """

        data_folder = Path("archives/mapper.json")
        file = open(data_folder)
        json_data = json.load(file)

        self.headers = {'Authorization': '123', 'Content-Type': 'application/json'}
        self.response = self.application.post('/mapper', json=json_data, headers=dict(self.headers))
        self.assertEqual(401, self.response.status_code)


    def test_content_eventid_json_body(self):
        """
        Nome: test content eventid in json body

        Descrição: 
            Testa se existe o valor
            eventid no json_body

        Args: self
        """

        data_folder = Path("archives/mapper.json")
        file = open(data_folder)
        json_data = json.load(file)

        self.assertIn('eventid', json_data)

    

    def test_no_content_eventid_json_body(self):
        """
        Nome: test no content eventid in json body

        Descrição: 
            Testa se não existe o valor
            eventid no json_body

        Args: self
        """

        data_folder = Path("archives/mapper_no_eventid.json")
        file = open(data_folder)
        json_data = json.load(file)

        self.headers = {'Authorization': '2j3k3o5p5i3p1p3oi',  'Content-Type': 'application/json'}
        self.response = self.application.post('/mapper', json=json_data, headers=dict(self.headers))

        self.assertEqual(404, self.response.status_code)


    def test_content_df_json_body(self):
        """
        Nome: test content df in json body

        Descrição: 
            Testa se existe o valor
            df no json_body

        Args: self
        """

        data_folder = Path("archives/mapper.json")
        file = open(data_folder)
        json_data = json.load(file)

        self.assertIn('df', json_data)

    def test_no_content_df_json_body(self):
        """
        Nome: test no content df in json body

        Descrição: 
            Testa se não existe o valor
            df no json_body

        Args: self
        """

        data_folder = Path("archives/mapper_no_df.json")
        file = open(data_folder)
        json_data = json.load(file)

        self.headers = {'Authorization': '2j3k3o5p5i3p1p3oi',  'Content-Type': 'application/json'}
        self.response = self.application.post('/mapper', json=json_data, headers=dict(self.headers))

        self.assertEqual(404, self.response.status_code)

    def test_method_put(self):
        """
        Nome: test method

        Descrição: 
            Testa se com método diferente
            o request funciona

        Args: self
        """


        data_folder = Path("archives/mapper.json")
        file = open(data_folder)
        json_data = json.load(file)

        self.headers = {'Authorization': '2j3k3o5p5i3p1p3oi', 'Content-Type': 'application/json'}
        self.response = self.application.put('/mapper', json=json_data, headers=dict(self.headers))

        self.assertEqual(405, self.response.status_code)

    def test_method_delete(self):
        """
        Nome: test method

        Descrição: 
            Testa se com método diferente
            o request funciona

        Args: self
        """


        data_folder = Path("archives/mapper.json")
        file = open(data_folder)
        json_data = json.load(file)

        self.headers = {'Authorization': '2j3k3o5p5i3p1p3oi', 'Content-Type': 'application/json'}
        self.response = self.application.delete('/mapper', json=json_data, headers=dict(self.headers))

        self.assertEqual(405, self.response.status_code)

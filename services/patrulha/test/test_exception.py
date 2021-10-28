"""
Arquivo de testes 

==================

Para rodar os testes basta
entrar na pasta tests
e make test

"""

from pytest import mark 
from src.decorators import exception

@exception
def funcao():
    broken
    pass

@mark.describe("Teste da API")
class Test_Exception(unittest.TestCase):
    """
    Testes para o decorator exception
    """
   
    def test_exception(self):
        """
        Testa se o decorator exception responde para código quebrado.
        """
            
        a = funcao()
        self.assertEqual(('Ocorreu um erro inesperado', 500, [('Access-Control-Allow-Origin', '*'), ('Access-Control-Allow-Headers', 'Content-Type,Authorization,X-Api-Key'), ('Access-Control-Allow-Methods', 'OPTIONS,POST')]),a)

        
        
      

    
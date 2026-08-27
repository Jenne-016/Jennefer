import pessoa
import unittest

class Teste(unittest.TestCase):
    def teste_idade(self):
        p = pessoa.Pessoa()
        p.Armazena("João", 25)
        self.assertEqual(p.idade, [25])
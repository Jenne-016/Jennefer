import unittest
import Pessoa

class TestePessoa(unittest.TestCase):

    def test_Pessoa(self):
        self.assertEqual(Pessoa.Pessoa.Nome("Jennefer Linda"), "Jennefer Linda")
        self.assertEqual(Pessoa.Pessoa.Idade("67"), "67")

if __name__ == '__main__':
    unittest.main(exit=False)
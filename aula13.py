class PessoaGeral:
    def __init__(self,idade,cor):
        self.idade=idade
        self.cor=cor

    def falar(self):
        print("Olá!")   

class Pessoa1(PessoaGeral):
    def __init__(self, idade, cor):
        super().__init__(idade, cor)
    def _falar(self):
        return "Olá, eu sou a pessoa 1!"

jorge=Pessoa1(idade=6,cor="branco")
print(jorge.cor,jorge.idade)
print(jorge.falar())
        
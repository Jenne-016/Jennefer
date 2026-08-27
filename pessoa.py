class Pessoa():
    def __init__(self):
        self.idade=[]
        self.nome=[]

    def Idade(self):
        print(self.idade)

    def Nome(self):
        print(self.nome)

    def Armazena(self,nome,idade):
        self.nome.append(nome)
        self.idade.append(idade)
        
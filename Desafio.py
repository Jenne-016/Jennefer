class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.informacoes = (
            "Nome=" + self.nome +
            ", Idade=" + str(self.idade) +
            ", Altura=" + str(self.altura)
        )


pessoa1 = Pessoa(nome="Alice", idade=30, altura=1.65)
pessoa2 = Pessoa(nome="José", idade=2, altura=80)

print(pessoa1.informacoes)
print(pessoa2.informacoes)

class Casa1():
    def __init__(self, rua, bairro, cep):
        self.rua = rua
        self.bairro = bairro
        self.cep = cep
        self.EnderecoCompleto = "Rua=" + self.rua + ", Bairro=" + self.bairro + ", CEP=" + self.cep
casa1 = Casa1(rua="A", bairro="dois", cep="11")
print(casa1.EnderecoCompleto)
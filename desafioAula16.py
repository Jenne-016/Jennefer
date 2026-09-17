def perguntaNome():
  while True:
    nome = input("Digite seu nome: ")
    if nome.isalpha():
      print("O nome digitado foi:", nome)
      break
perguntaNome()
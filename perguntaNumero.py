def pergunta_numero():
    tentativa=1
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
        except ValueError:
            print("Você não digitou um número válido.")
            continue
        else:
            break
        finally:
            print("Tentativa numero:", tentativa)
            tentativa += 1

    print(numero)

pergunta_numero()
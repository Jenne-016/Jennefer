def saudacoes(nome_usuario,nome_bot):
    print(f"Olá, {nome_usuario}! Bem-vindo ao nosso chatbot {nome_bot}.")
    frases = ["Como posso ajudá-lo?"]
    print(frases[0])
    print("Digite sair a qualquer momento para encerrar a conversa.")


def recebeTexto():
    texto = input("Digite algo: ")

    palavrasProibidas = ["bobalhao"]

    for palavra in palavrasProibidas:
        if palavra in texto.lower():
            print("Palavra proibida detectada! Por favor, evite usar palavras ofensivas.")
            return recebeTexto()

    return texto


def buscaResposta(texto):
    respostas = [
        ("oi", "Oi! Como você está?"),
        ("tchau", "Tchau! Tenha um bom dia!"),
        ("como vai?", "Estou bem, obrigado por perguntar!"),
        ("qual é o seu nome?", "Eu sou um chatbot criado para ajudá-lo."),
        ("qual é a sua função?", "Minha função é responder suas perguntas e ajudá-lo com informações."),
        ("obrigado", "De nada! Estou aqui para ajudar."),
        ("desculpe", "Não se preocupe! Todos cometemos erros."),
        ("ajuda", "Claro! Estou aqui para ajudar. O que você precisa?"),
        ("informações", "Posso fornecer informações sobre diversos assuntos. Sobre o que você quer saber?"),
        ("ok", "ok")
    ]

    texto = texto.lower()

    for chave, resposta in respostas:
        if chave in texto:
            return resposta

    return "Desculpe, não entendi. Pode reformular a pergunta."


# Programa principal
nome_usuario = input("Digite seu nome: ")
nome_bot = input("Digite o nome do chatbot: ")
saudacoes(nome_usuario, nome_bot)

while True:
    texto = recebeTexto()

    if texto.lower() == "sair":
        print("Até logo!")
        break

    resposta = buscaResposta(texto)
    print(resposta)

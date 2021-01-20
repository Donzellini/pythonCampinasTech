#source: https://academiahopper.com.br/dicionarios-em-python/

command = "continue"
contacts = {}

def procura_chaves(dicionario, nome):
    chaves = []
    for chave in dicionario:
        if chave.startswith(nome):
            chaves.append(chave)
    return chaves

while command != "sair":
    command = input("Escolha uma opção: (novo, pes, sair):")

    if command == "novo":
        nome = input("Nome: ").strip()
        telefone = input("Telefone: ").strip()
        email = input("E-mail: ").strip()
        contacts[nome] = {
            "nome": nome,
            "telefone": telefone,
            "email": email
        }

    if command == "pes":
        nome = input("Nome: ").lower()
        chaves_encontradas = procura_chaves(contacts, nome)

        if len(chaves_encontradas) > 0:
            for chave in chaves_encontradas:
                print(contacts[chave])

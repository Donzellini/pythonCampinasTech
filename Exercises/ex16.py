# 16. Fazer um sistema de Agenda de contatos (Deve criar um dicionário com Nome, Telefone e Endereço, Imprimir os dados do dicionário, ser capaz de inserir e excluir um contato)
# source: https://academiahopper.com.br/dicionarios-em-python/

agenda = []


def inserir_nome():
    return(input("Nome da pessoa que deseja adicionar: "))


def inserir_telefone():
    return(input("Insira seu numero de telefone: "))


def inserir_endereco():
    return(input("Insira o endereço: "))


def adicionar():
    global agenda
    nome = inserir_nome()
    telefone = inserir_telefone()
    endereco = inserir_endereco()
    agenda.append([nome, telefone, endereco])


def adicionar1():
    nome_arquivo = inserir_nome()
    arquivo = open(nome_arquivo, "w", encoding="utf-8")
    for e in agenda:
        arquivo.write("Nome: %s Telefone: %s Endereço: %s\n" % (e[0], e[1], e[2]))
    arquivo.close()

print("\n-------------------------------")
print("Bem-vindo a sua agenda!")
print("-------------------------------")

print("Escolha o tipo de operação")

operacoes = input('''
Para adicionar digite " adicionar "!
''')

if operacoes == 'adicionar':
    print("\nOpção ADICIONAR selecionada")
    adicionar()
    adicionar1()
    inserir_telefone()
    inserir_endereco()

else:
    print('Você nao digitou um valor aceitavel!')
    print("Fim de operação!")

print("Fim de operação!")
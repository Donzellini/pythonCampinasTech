from agenda import agenda

lista_opcoes = ["Novo Contato", "Visualizar Agenda", "Excluir Contato", "Sair"]
lista_contatos = []
i = 0
t = len(lista_opcoes) - 1
opcao = 0

#cabeçalho do programa
def cabecalho():
    print("----------------------------")
    print("           AGENDA")
    print("----------------------------")

def sair():
    print("Saindo!")

def opcao_invalida():
    print("Digite uma opção válida.")
    
def novo_contato(agenda):
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")
    lista_contatos.append([nome, telefone, endereco])

def visualizar_agenda():
    indice = 0
    for item in lista_contatos:
        print(f"{indice} - {item}")
        indice += 1

def excluir_contato():
    visualizar_agenda()
    item_deletado = int(input("Deletar item: "))
    resposta = 0
    while resposta != "N":
        if item_deletado in range(0, len(lista_contatos)):
            lista_contatos.pop(item_deletado)
            visualizar_agenda()
            resposta = input("Deletar outro contato? (S/N): ")
        else:
            opcao_invalida()
            if resposta == "S":
                excluir_contato()
            else:
                opcao_invalida()
#contador da lista de opções
cabecalho()

while i <= t:
    for num in lista_opcoes:
        print(f"[{i}] {num}")
        i += 1
#leitor do input e trigger para as funções
while opcao != 3:
    opcao = int(input("OPÇÃO: "))

    if opcao == 0:
        novo_contato(agenda)
        # armazena_dados()
    
    if opcao == 1:
        visualizar_agenda()

    if opcao == 2:
        excluir_contato()

    if opcao == 3:
        sair()
        
else:
    opcao_invalida()
print("----------------------------")
print("           AGENDA")
print("----------------------------")
#variáveis globais
lista_opcoes = ["Novo Contato", "Visualizar Agenda", "Excluir Contato", "Sair"]
lista_contatos = []
agenda = {}
i = 0
t = len(lista_opcoes) - 1
opcao = 0
#funções
def sair():
    print("Saindo!")

def opcao_invalida():
    print("Digite uma opção válida.")

def novo_contato():
    global agenda
    agenda['nome'] = (input("Nome: "))
    agenda['telefone'] = (input("Telefone: "))
    agenda['endereco'] = (input("Endereço: "))
    armazena_dados()

def armazena_dados():    
    nome = agenda['nome']
    telefone = agenda['telefone']
    endereco = agenda['endereco']
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
            item_selecionado = lista_contatos.pop(item_deletado)
            visualizar_agenda()
            resposta = input("Deletar outro contato? (S/N): ")
        else:
            opcao_invalida()
            if resposta == "S":
                excluir_contato()
            else:
                opcao_invalida()
#contador da lista de opções
while i <= t:
    for num in lista_opcoes:
        print(f"[{i}] {num}")
        i += 1
#leitor do input e trigger para as funções
while opcao != 3:
    opcao = int(input("OPÇÃO: "))

    if opcao == 0:
        novo_contato()
    
    if opcao == 1:
        visualizar_agenda()

    if opcao == 2:
        excluir_contato()

    if opcao == 3:
        sair()
        
    else:
        opcao_invalida()
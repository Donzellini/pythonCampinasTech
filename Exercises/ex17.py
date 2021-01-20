print("----------------------------")
print("       REVISÃO DE AUTO")
print("----------------------------")
#variáveis globais
lista_opcoes = ["Agendar Revisão", "Visualizar Agenda", "Sair"]
lista_agendamentos = []
agenda = {}
opcao = 0

#funções
def listagem():
    i = 0
    t = len(lista_opcoes) - 1
    while i <= t:
        for num in lista_opcoes:
            print(f"[{i}] {num}")
            i += 1

def sair():
    print("Saindo!")

def opcao_invalida():
    print("Digite uma opção válida.")

def agendar_revisao():
    global agenda
    agenda['proprietario'] = (input("Proprietário: "))
    agenda['modelo'] = (input("Modelo: "))
    agenda['ano'] = (input("Ano: "))
    agenda['data'] = (input("Data: "))
    agenda['hora'] = (input("Hora: "))
    armazena_dados()

def armazena_dados():    
    proprietario = agenda['proprietario']
    modelo = agenda['modelo']
    ano = agenda['ano']
    data = agenda['data']
    hora = agenda['hora']
    lista_agendamentos.append([proprietario, modelo, ano, data, hora])

def visualizar_agenda():
    indice = 0
    for item in lista_agendamentos:
        print(f"{indice} - {item}")
        indice += 1

listagem()

#leitor do input e trigger para as funções
while opcao != 3:
    opcao = int(input("OPÇÃO: "))

    if opcao == 0:
        agendar_revisao()
        listagem()

    if opcao == 1:
        visualizar_agenda()

    if opcao == 2:
        sair()
        break
else:
    opcao_invalida()
    listagem()
    
print("----------------------------")
print("       FEIRA DA FRUTA")
print("----------------------------")
#variáveis globais
lista_opcoes = ["Ver Produtos", "Comprar", "Sair"]
lista_compra = []
dict1 = {'produto': 'morango', 'preço':"R$4,50"}
dict2 = {'produto': 'abacaxi', 'preço':"R$6,00"}
dict3 = {'produto': 'lichia', 'preço':"R$10,00"}
opcao = 0
print(dict1)

# funções
def listagem():
    i = 0
    t = len(lista_opcoes) - 1
    while i <= t:
        for num in lista_opcoes:
            print(f"[{i}] {num}")
            i += 1

# def sair():
#     print("Saindo!")

# def opcao_invalida():
#     print("Digite uma opção válida.")

def produtos():
    c1 = 1
    c2 = 2
    c3 = 3
    print(f"[{c1}] {dict1}")
    print(f"[{c2}] {dict2}")
    print(f"[{c3}] {dict3}")
    print("")

# def comprar():    
#     produto1 = (item1[1])
#     preco1 = (item1[2])
#     produto2 = (item1[1])
#     preco2 = (item1[2])
#     produto3 = (item1[1])
#     preco3 = (item1[2])
#     lista_compra.append([produto, preco])

# def visualizar_agenda():
#     indice = 0
#     for item in lista_compra:
#         print(f"{indice} - {item}")
#         indice += 1

listagem()

#leitor do input e trigger para as funções
while opcao != 3:
    opcao = int(input("OPÇÃO: "))

    if opcao == 0:
        produtos()
        listagem()

    if opcao == 1:
        visualizar_agenda()

    if opcao == 2:
        sair()
        break
else:
    opcao_invalida()
    listagem()
    
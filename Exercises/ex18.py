print("----------------------------")
print("       FEIRA DA FRUTA")
print("----------------------------")
#variáveis globais
lista_opcoes = ["Ver Produtos", "Comprar", "Total", "Sair"]
lista_compra = []
total_compra = []
dict1 = [{'item': 0, 'produto': 'morango', 'preco': 4.50}, 
         {'item': 1, 'produto': 'abacaxi', 'preco': 6.00}, 
         {'item': 2,'produto': 'lichia', 'preco': 10.00}]
opcao = 0
print(dict1[0]['produto'])

# funções
# lista as opções do menu
def listagem():
    i = 0
    t = len(lista_opcoes) - 1
    while i <= t:
        for num in lista_opcoes:
            print(f"[{i}] {num}")
            i += 1

#opção sair
def sair():
    print("Saindo!")

#opção inválida
def opcao_invalida():
    print("Digite uma opção válida.")

#lista os produtos cadastrados no dicionário que pode virar um .json
def produtos():
    print(dict1)

#menu de compras
#sugestão: deseja continuar comprado? (S/N)
def comprar():
    print(dict1)
    item = int(input("Escolha um dos produtos acima: "))
    if item == dict1[item]['item']:
        lista_compra.append([dict1[item]])
        total_compra.append([dict1[item]['preco']])
    print("Sua lista de compras está abaixo: ")
    print(lista_compra)

#soma os valores numéricos da lista total_compras, gerada na def comprar()
def total():
    print(f'O total da sua compra é: {sum([ item[0] for item in total_compra])}')

listagem()

#leitor do input e trigger para as funções
while opcao != 3:
    opcao = int(input("OPÇÃO: "))

    if opcao == 0:
        produtos()
        listagem()

    if opcao == 1:
        comprar()
        listagem()
    
    if opcao == 2:
        total()
        listagem()

    if opcao == 3:
        sair()
        break
else:
    opcao_invalida()
    listagem()
    
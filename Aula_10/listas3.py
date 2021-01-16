# list1 = ['physics', 'chemistry', 1997, 2000]
# print(list1)
# del list1[2],list1[1] #é possível excluir mais de 1 item
# print("After deleting value at index 2: ")
# print(list1)

# utilizando o del, a lista é movida. se tiver 5 posições, após o del terá 4

# list2 = ['banana', 'maçã', 'abacaxi', 'uva', 'morango']

# list2.remove('maçã')
# list2.remove('abacaxi')
# # list2.remove('abacaxiiiii')
# list2.append('cereja')
# list2.append('laranja')
# list2.insert(2, 'pêssego') #recebe dois argumentos, o índice e o item a ser inserido
# print(list2)

lista_carros = ["ka", "ecosport", "fox", "gol"]

print(lista_carros)
lista_carros.insert(1, "renegade")
print(lista_carros)
del lista_carros[2:3] #removendo mais de um item utilizando range
print(lista_carros)
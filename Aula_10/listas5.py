lista_suco = ['laranja', 'uva', 'abacaxi', 'manga']
tupla_suco = ['laranja', 'uva', 'abacaxi', 'manga']

lista_refrigerantes = ['coca', 'guaraná', 'laranja', 'uva']
#não existe cmp do python 3
#print(cmp(lista_refrigerantes, lista_suco))
# print(max(lista_suco))
# print(min(lista_suco))
# print(len(lista_suco))
# print(type(list(tupla_suco)))

lista_suco2 = ['laranja', 'uva', 'abacaxi', 'abacaxi' 'manga']
#conta quantas vezes tem um elemento
#print(lista_suco2.count('abacaxi'))
#TODO: revisar a função extend no python 3

lista_suco.extend(lista_suco2)
print(lista_suco)
#resultado do extend
# lista3 = lista_suco + lista_suco2
# print(lista3)

# print(lista3.pop(4))
# print(lista3)

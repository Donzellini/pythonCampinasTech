#7. Fazer um sistema de Loteria (Deve pedir o nome do usuário, pedir um número e comparar com um conjunto aleatório de número (de 0 a 100) e dizer se o usuário advinhou)

#_________________________________________________
# PRIMEIRO INÍCIO DE SOLUÇÃO
# import random

# Criar uma lista com 100 elementos inteiros randômicos

# lista = list(range(1,101))

# print(lista)

# Embaralha a lista de números 
# random.shuffle(lista)

# print(lista)

# from random import randint
# lista = list(randint(range(1,101))100)
#_________________________________________________

#_________________________________________________
# SEGUNDO INÍCIO DE SOLUÇÃO
# Função que gera números aleatórios com determinada length
# Não consegui encontrar como inserir números inteiros

# def gerar():
#    from random import random
#    tamanho = 10
#    resposta = [1] * tamanho
#    for i in range(tamanho):
#        resposta[i] = random()
#    return resposta

# print(gerar())
#_________________________________________________

#_________________________________________________
# TERCEIRO INÍCIO DE SOLULÃO
# Há um problema nessa lógica, falta o computador selecionar um número dentro da lista para que funcione
# Caso o computador não "pense" em um número, e o usuário souber que o intervalo é de 1 a 100, ele sempre acertará o número

# from random import choices, sample

# tamanho = 100
# valores = range(1, 101)

# print(choices(valores, k=tamanho))
# print(sample(valores, tamanho))
#_________________________________________________

#_________________________________________________
# QUARTO INÍCIO DE SOLUÇÃO
# O computador pensa em número de 0 a 100, selecionando apenas 1
# O usuário deve acertar

import random

num = int(input("Foi sorteado um número de 0 a 100. Qual número você irá escolher? "))
sorteio = random.randint(0, 101)
print(sorteio)

if num == sorteio:
    print('Parabéns, o número sorteado foi {}.'.format(sorteio))
else:
    print('Não foi dessa vez, quem sabe da próxima vez...')
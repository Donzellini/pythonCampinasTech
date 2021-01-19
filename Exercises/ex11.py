#11. Fazer uma busca sequencial em uma matriz (Criar uma matriz 10 linhas e 10 colunas e pedir para o usuário fazer uma busca)

import numpy as np #recurso do python para imprimir a matriz em formato tridimensional

#função para gerar a matriz
# def gerar_matriz (n_colunas, n_linhas):
#     matriz = []

# #contador for para gerar a matriz
#     for i in range(n_linhas):
#         matriz.append( [i + 1] * n_colunas )
#     return matriz

#adicionei na variável a função que gera a matriz. aqui eu delimitei o tamanho da matriz (10x10)

m2 = [list(range(i, i+10)) for i in range(1, 100, 10)] #usando list comprehension

#printando a matriz no formato de matriz utilizando o numpy
print (np.matrix(m2))

choice = int(input("Escolha uma opção dentro da matriz acima: "))

i = 1 #contador de linha
j = 1 #contador de coluna
isencontrado = False #Flag para verificar se o dado foi encontrado
for linha in m2: #varre a linha da Matriz
    for coluna in linha: #varre a coluna da linha da Matriz
        if(coluna == choice): #Compara para fazer a busca
            print(f"Encontrou {coluna} na linha {i} e na coluna {j}.")
            isencontrado = True
            break
        j += 1
    if isencontrado:
        break
    i += 1
    j = 1 #reset de coluna

if isencontrado == False:
    print("Dado não encontrado")
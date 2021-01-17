#11. Fazer uma busca sequencial em uma matriz (Criar uma matriz 10 linhas e 10 colunas e pedir para o usuário fazer uma busca)

import random #estava pensando em randomizar os números dentro da matriz, mas não consegui aplicá-lo
import numpy as np #recurso do python para imprimir a matriz em formato tridimensional

#função para gerar a matriz
def gerar_matriz (n_colunas, n_linhas):
    matriz = []

#contador for para gerar a matriz
    for i in range(n_linhas):
        matriz.append( [i + 1] * n_colunas )
    return matriz

#adicionei a variável a função que gera a matriz. aqui eu delimitei o tamanho da matriz (10x10)
m2 = (gerar_matriz(10, 10))

#printando a matriz no formato de matriz utilizando o numpy
print (np.matrix(m2))

opcao = list(input("Escolha uma opção dentro da matriz acima: "))

#tentei usar a mesma lógica do exercício 10, mas não está funcionando
#pula direto para a última opção da estrutura for

def busca (m2, opcao):
    for x in m2:
        if x == opcao:
            print("Elemento {} está presente na matriz.".format(opcao))
            return
    print("Elemento {} não está presente na matriz.".format(opcao)) 

busca(m2, opcao)
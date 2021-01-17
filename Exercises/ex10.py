#10. Fazer uma busca sequencial em uma lista (Criar uma tupla [0....20] e pedir para o usuário fazer uma busca)
#source: https://algoritmosempython.com.br/cursos/algoritmos-python/pesquisa-ordenacao/pesquisa-linear/

#criando a tupla com opções numéricas, poderia ser qualquer outra opção
tup = tuple(range(1, 21))
print(tup)

#coleta o input do usuário
opcao = int(input("Escolha uma opção dentro da lista acima: "))

#função para busca linear
def busca(tup, opcao):
    for elemento in tup:
        if elemento == opcao:
            print("Elemento {} está presente na tupla.".format(opcao))
            return
    print("Elemento {} não está presente na tupla.".format(opcao))

#chama a função buscando se o elemento escolhido está presente.
busca(tup, opcao)

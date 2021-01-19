# 15. Fazer um sistema de Feira Livre(Deve imprimir uma lista com as frutas e pedir para o solicitante colocar o nome e selecionar a fruta e depois deve imprimir o nome do solicitante e a fruta)

list_fruits = ["banana","apple","pineapple","strawberry","peach"]

i = 0
t = len(list_fruits) - 1 #tratei a variável com -1 para pode usá-la na estrutura while

while i <= t: #o loop percorrerá t, ou seja, o tamanho da lista, enquanto incrementa i
    for fruit in list_fruits: 
        print(f"[{i}] {fruit}") 
        i = i + 1

name = input("Como devo lhe chamar? ")

chosen_fruit = int(input(f"{name}, você deve escolher uma das frutas acima para comprar: "))

if chosen_fruit in range(0, 5):
    print(f"{name}, você escolheu {list_fruits[chosen_fruit]}")
else:
    print(f"{name}, você deve escolher uma opção válida.")
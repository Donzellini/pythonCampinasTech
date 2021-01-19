# 13. Fazer um cadastro de viagem (Deve pedir o nome do viajante, dar as opções de destino e imprimir a selecionada)

name = input("Olá! Qual é o seu nome? ")
list_places = ["Japão","Croácia", "Espanha","Noruega"]

i = 0
t = len(list_places) - 1 #tratei a variável com -1 para pode usá-la na estrutura while

while i <= t: #o loop percorrerá t, ou seja, o tamanho da lista, enquanto incrementa i
    for place in list_places: 
        print(f"[{i}] {place}") 
        i = i + 1

chosen_place = int(input("Você deve escolher um dos locais acima para viajar: "))

if chosen_place in range(0, 4):
    print(f"{name}, você irá para {list_places[chosen_place]}")
else:
    print(f"{name}, você deve escolher uma opção válida.")
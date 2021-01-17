# 13. Fazer um cadastro de viagem (Deve pedir o nome do viajante, dar as opções de destino e imprimir a selecionada)

name = input("Olá! Qual é o seu nome? ")
list_places = ["Japão","Croácia", "Espanha","Noruega"]

for place in list_places:
    print(f"- {place}")

chosen_place = input("Você deve escolher um dos locais acima para viajar: ")

print(f"{name}, você irá para {chosen_place}")

#sugestão: adicionar opções numéricas aos locais depois
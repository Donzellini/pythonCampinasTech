# 15. Fazer um sistema de Feira Livre(Deve imprimir uma lista com as frutas e pedir para o solicitante colocar o nome e selecionar a fruta e depois deve imprimir o nome do solicitante e a fruta)

list_fruits = ["banana","apple","pineapple","strawberry","peach"]

for fruit in list_fruits:
    print(f"- {fruit}")

name = input("Olá! Qual é o seu nome? ")

chosen_fruit = input("Você deve escolher uma das frutas acima para compra: ")

print(f"{name}, você irá comprar {chosen_fruit}.")

#mesma sugestão dos ex13 e 14
#fazer um método para o solicitante comprar quantas frutas quiser
#colocar um verificador se a fruta está na lista.
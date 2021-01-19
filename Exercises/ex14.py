# Fazer um sistema de biblioteca (Deve imprimir uma lista com 10 livros, pedir o nome do solicitante do empréstimo, pedir para selecionar um livro e imprimir o livro selecionado)

name = input("Olá! Qual é o seu nome? ")
list_books = ["Ana Karenina","A roda do tempo", "Senhor dos Aneis vol.1","Senhor dos Aneis vol.2","Senhor dos Aneis vol.3","Como treinar seu dragão","The Witcher vol.1","The Witcher vol.2","The Witcher vol.3","O poeta e o cavaleiro"]

i = 0
t = len(list_books) - 1 #tratei a variável com -1 para pode usá-la na estrutura while

while i <= t: #o loop percorrerá t, ou seja, o tamanho da lista, enquanto incrementa i
    for book in list_books: 
        print(f"[{i}] {book}") 
        i = i + 1

chosen_book = int(input("Você deve escolher um dos livros acima para o empréstimo: "))

if chosen_book in range(0, 10):
    print(f"{name}, você escolheu {list_books[chosen_book]}")
else:
    print(f"{name}, você deve escolher uma opção válida.")
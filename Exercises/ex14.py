# Fazer um sistema de biblioteca (Deve imprimir uma lista com 10 livros, pedir o nome do solicitante do empréstimo, pedir para selecionar um livro e imprimir o livro selecionado)

name = input("Olá! Qual é o seu nome? ")
list_books = ["Ana Karenina","A roda do tempo", "Senhor dos Aneis vol.1","Senhor dos Aneis vol.2","Senhor dos Aneis vol.3","Como treinar seu dragão","The Witcher vol.1","The Witcher vol.2","The Witcher vol.3","O poeta e o cavaleiro"]

for book in list_books:
    print(f"- {book}")

chosen_book = input("Você deve escolher um dos livros acima para o empréstimo: ")

print(f"{name}, o livro selecionado é {chosen_book}")

#mesma sugestão do ex13
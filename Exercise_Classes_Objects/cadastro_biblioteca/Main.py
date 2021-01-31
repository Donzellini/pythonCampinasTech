from Book import Book

name = input("Olá! Qual é o seu nome? ")
list_books = ["Ana Karenina","A roda do tempo", "Senhor dos Aneis vol.1","Senhor dos Aneis vol.2","Senhor dos Aneis vol.3","Como treinar seu dragão","The Witcher vol.1","The Witcher vol.2","The Witcher vol.3","O poeta e o cavaleiro"]
list_chosen_books = []

i = 0
t = len(list_books)

while i < t: #o loop percorrerá t, ou seja, o tamanho da lista, enquanto incrementa i
    for book in list_books: 
        print(f"[{i}] {book}") 
        i += 1 #mudei o tipo de incremento que eu fiz na primeira lista de exercícios

chosen_book = int(input(f"{name}, você deve escolher um dos livros acima para o empréstimo: "))
book = Book(book=list_books[chosen_book])
list_chosen_books.append(book.book)

if chosen_book in range(0, 10):
    print(f"{name}, você escolheu {list_chosen_books}")
else:
    print(f"{name}, você deve escolher uma opção válida.")

#melhoria: fazer um elif para ver se o usuário quer locar mais de um livro, a estrutura append já está pronta para receber esse tipo de comando
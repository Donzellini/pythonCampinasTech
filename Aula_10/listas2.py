list = ['physics', 'chemistry', 1997, 2000]
print("Value available at index 2: ")
print(list[2])
list[2] = 2001
print("New value available at index 2: ")
print(list[2])

list.append("hahahah") #sempre adiciona no final
list.append(1000)
list.append(["ajajajaj", 1234]) #lista dentro de lista
list.append({'Chave':'valor','OutraChave':'OutroValor'}) #adicionando dicionário

print(list)
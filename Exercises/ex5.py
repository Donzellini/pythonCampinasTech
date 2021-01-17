#5. Algoritmo para calcular a média do aluno (Deve colocar o nome do aluno, colocar 4 notas e imprimir sua média)

print("MÉDIA DO ALUNO")
print("________________")
print("")
nome = (input("Digite o nome do aluno: "))
n1 = int(input("Digite a 1ª nota: "))
n2 = int(input("Digite a 2ª nota: "))
n3 = int(input("Digite a 3ª nota: "))
n4 = int(input("Digite a 4ª nota: "))
media = (n1 + n2 + n3 + n4)/4
print(f"A média de {nome} é: {media}")
#8. Elabore um algoritmo em Python que receba um número inteiro e escreva na tela o número fornecido, o antecessor desse número e o sucessor desse número;

num_ins = int(input("Digite um número inteiro: "))
num_ant = num_ins - 1 
num_suc = num_ins + 1

# verificando as variáveis criadas
# print (num_ant)
# print (num_suc)

print (f"O número digitado foi {num_ins}. O número antecessor ao digitado é {num_ant}. O número sucessor ao digitado é {num_suc}.")

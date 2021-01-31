def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return

def calcula_soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado


num1 = int(input("Digite o número 1 \n"))
num2 = int(input("Digite o número 2 \n"))

resul = calcula_soma(numero1=num1,numero2=num2)

print(f"O resultado é {resul}")


from employee import Employee
from persona import Persona

nome = input("Coloque o nome do empregado \n")
salario = float(input("Coloque o seu salário \n"))

pessoa = Persona(nombre="Je", sueldo=0) #a ordem dos parâmetros não vai importar desde que o parâmetro seja especificado
print(f"O nome é {pessoa.nombre}")

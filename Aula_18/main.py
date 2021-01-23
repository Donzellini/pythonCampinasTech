from employee import Employee
from persona import Persona

# nome = input("Coloque o nome do empregado \n")
# salario = float(input("Coloque o seu salário \n"))

pessoa = Persona(nombre="Je", sueldo=0) #a ordem dos parâmetros não vai importar desde que o parâmetro seja especificado
print(f"O nome é {pessoa.nombre}")

# - The **getattr(obj, name[, default])** − to access the attribute of object.
# - The **hasattr(obj,name)** − to check if an attribute exists or not.
# - The **setattr(obj,name,value)** − to set an attribute. If attribute does not exist, then it would be created.
# - The **delattr(obj, name)** − to delete an attribute.

emp = Employee("Jeff", 10) #Criando o objeto
# Todas as funções abaixo trabalham em cima do objeto não da classe
# hasattr(emp, 'name')    # Returns true if 'name' attribute exists
# getattr(emp, 'name')    # Returns value of 'name' attribute
# setattr(emp, 'name', "Jefinho") # Set attribute 'name' to Jefinho
# delattr(emp, 'name')    # Delete attribute 'name'
# ```
print(emp.name) #Pegando o valor do atributo/campo
print(getattr(emp, 'name')) #Pegando o valor do atributo/campo
print(hasattr(emp, 'nameaaa')) #Verificando se o atributo/campo existe
setattr(emp, 'name', "Jefinho") #Atribuir valor para o campo name
print(emp.name) #Conferindo a mudança
# delattr(emp, 'name') #Excluí o atributo do objeto (da instância)
print(emp.name) #Conferindo a mudança

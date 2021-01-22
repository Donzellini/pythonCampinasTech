class Employee:
   'Common base class for all employees'
   empCount = 0
	

   def __init__(self, name, salary): #boa prática usar o .self
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print("Name : ", self.name,  ", Salary: ", self.salary)

#solicitando valores no terminal
nome = input("coloque o nome do empregado \n")
salario = float(input("Coloque o seu salário \n"))
#criando objeto employee
novo_empregado = Employee(name=nome,salary=salario)
print(f"o nome do empregado é {novo_empregado.name}")
print(f"e o seu salario é {novo_empregado.salary}")
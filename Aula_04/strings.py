#!/usr/bin/python

str = 'Hello World!'

print(str)          # Prints complete string
print(str[0])       # Prints first character of the string
print(str[2:5])     # Prints characters starting from 3rd to 5th
print(str[2:])      # Prints string starting from 3rd character
print(str * 2)      # Prints string two times
print(str + "TEST") # Prints concatenated string

#ensinando a interpolação de strings

nome = "Muriel"

texto = f"A {nome} é uma pessoa bacana" #aqui tem o comando para interpolação

print(texto)
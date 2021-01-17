#9. Elabore um algoritmo em Python que calcule a área e o perímetro de um círculo, sabendo que A = πr² e P=2πr.

pi = 3.14
r = float(input("Insira o raio do círculo em m: "))
a = pi * (r**2)
p = 2 * pi * r

#usei o recurso .format para limitar as casas decimais em 2
print(f'A área do círculo é {a:.2f} e o perímetro é {p:.2f}'.format(a, p))
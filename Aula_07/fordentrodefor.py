lista_uma_dimensao = ["a","b","c"]

#                 p   p   p
#                 o   o   o
#                 s   s   s
#                 i   i   i
#                 ç   ç   ç
#                 ã   ã   ã
#                 o   o   o
#                 0   1   2

lista_matriz = [["a","b","c"], #posição 0
                ["d","e","f"], #posição 1
                ["g","h","i"]] #posição 2

for it1 in lista_matriz: #loop dentro de loop (for)
    print(it1)
    for it2 in it1:
        print(f"O item é: {it2}")
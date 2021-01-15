nome = "João"
iteracao = 0

print("começo programa")

while iteracao <= 10:
    iteracao = iteracao + 1
    if iteracao == 4:
        break
    print(f"Meu nome é {nome} {iteracao}")
    #iteracao += 1

print("fim programa")

print("começo programa")

while iteracao <= 10:
    iteracao = iteracao + 1
    if iteracao == 4:
        continue
    print(f"Meu nome é {nome} {iteracao}")
    #iteracao += 1

print("fim programa")

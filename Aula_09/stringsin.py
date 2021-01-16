var = "hello python"
letra = input(f"A string é {var}... Digite uma letra para busca...")

if len(letra) ==1:
    if letra in var:
        print(f"A letra {letra} existe")
    else:
        print(f"A letra {letra} não existe")
elif len(letra) > 1:
    print("VocÊ digitou mais que um caractere. A busca será cancelada!")
else:
    print("Você não digitou uma letra!")
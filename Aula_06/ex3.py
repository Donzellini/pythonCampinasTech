nome = "Jeff"
pessoa = "Professor"
ispessoa = True


if pessoa == "Aluno":
    print("É aluno")
    if ispessoa == True:
        print(f"Olá {nome}!")
    else:
        print("Olá Alguém!")

elif pessoa == "Professor":
    print("É professor")
    if ispessoa:
        print(f"Olá {nome}!")
    else:
        print("Olá Alguém!")
elif pessoa == "Aprendiz":
    print("Olá Aprendiz")

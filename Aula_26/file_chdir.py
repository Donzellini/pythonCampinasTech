import os

# os.chdir("C:\\CursoPython\\Aula_18\\teste")

#se usar o r (raw), funciona o caminho sem \\, no windows, mas não aceita interpolação de strings

nome_diretorio = "test"
# Changing a directory to "/home/newdir"
os.chdir(f"C:\CursoPython\Aula_18\{nome_diretorio}")

if os.getcwd() == f"C:\CursoPython\Aula_18\{nome_diretorio}":
    print("beleza!!!!")

print(os.getcwd())

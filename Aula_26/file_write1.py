frutas = ["banana", "laranja", "limão", "cereja"]

fo = open("frutas.txt", "w")

for fruta in frutas:
    fo.write(f'{fruta} \n')

fo.close()
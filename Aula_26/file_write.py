# fo = open("foo.txt", "w")

# fo.write("Python is a great language. \nYeah it great!!\n")

# fo.close()

fo = open("foo.txt", "r+") #read é pra ler
str = fo.readline() #lê apenas uma linha, o read apenas pode ser perigoso, imagina um arquivo txt de 3GB...
print ("Read string is : ", str)

fo.close()
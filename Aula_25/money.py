Money = 2000
def AddMoney():
    global Money #pux a variável global pra dentro da função, não preciso criar outra variavel local.
    Money += 1

print(Money)
AddMoney()
print(Money)

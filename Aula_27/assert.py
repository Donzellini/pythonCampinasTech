def KelvinToFahrenheit(Temperature):
   #assert (Temperature >= 0),"Colder than absolute zero!"
   if Temperature >= 0:
        return ((Temperature-273)*1.8)+32

# print (KelvinToFahrenheit(273))
# print (int(KelvinToFahrenheit(505.78)))
# print (KelvinToFahrenheit(-5))


def imprime_nome(nome):
    assert (nome != "Jeff")    , "O nome tem que ser diferente de Jeff" 
    assert (nome != "João")    , "O nome tem que ser diferente de João"
    print(nome)

#imprime_nome("Jeff")
imprime_nome("João")

def temp_convert(var):
    try:
        return int(var)
    except ValueError as Argument:
        print ("fofinho, os argumentos não são númros queridinho, \n", Argument)

temp_convert("xyz")
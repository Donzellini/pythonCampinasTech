def functionName( level ):
    if level <1:
        raise Exception(level, "xiiiiiiiiii")
    #the code below to this would not be exdcuted if we raise the exception
    return level


try:
    l = functionName(-10)
    print ("level = ", 1)
except Exception as e:
    print("fofinho, deu erro... olha o valor",e.args[0], e.args[1])
#exemplo de utlização do j (para números com raiz negativa)

def calcular_baskhara(a,b,c):
    z=(b ** 2) - (4 * a * c)
    if z<0:

        delta=(sqrtcomplex((z)))
        z1 = complex((-b / (2 * a)) + (delta / (2 * a)))
        z2 = complex((-b / (2 * a)) - (delta / (2 * a)))
        return (z1, z2)
    else:
        delta=sqrt(z)
    if delta==0:
        x=-b/(2*a)
        return x
    elif delta>0:
        x1=(-b+delta)/(2*a)
        x2=(-b-delta)/(2*a)
        return (x1,x2)

print(calcular_baskhara(1,-14,50))

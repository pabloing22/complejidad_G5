from decorators import delta_time


def allDivisores(n):
    return ('todos los divisores de: ',n)


def amigos(n):
    divisores=allDivisores(n)
    return divisores

# print(amigos(100))

n=[220,284,1184,1210,2620,2924,5020,5564,6232,6368,10744,10856,12285,14595,17296,18416,63020,76084,66928,66992,67095,71145,69615,87633,79750,88730]

prim=[2,3,5,7]


def calc(n,arreglo):
    if(n==1):
        return arreglo
    else:
        m=n
        if(n%2==0):
            m=2
        elif (n%3==0):
            m=3
        elif (n%5==0):
            m=5
        elif (n%7==0):
            m=7
        elif (n%11==0):
            m=11
        arreglo.append(m)
        return calc(n//m,arreglo)



print(calc(220,[]))
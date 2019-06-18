from decorators import delta_time


def divisores(n):
    sum=0
    # top=(n // 2)+1
    # if(n % 2==0):
    #     top=(n // 2)+1
    # elif(n % 3 == 0):
    #     top=(n // 3)+1
    # elif (n % 5 == 0):
    #     top=(n // 5)+1
    # elif (n % 7 == 0):
    #     top=(n // 7)+1
    # elif (n % 11 == 0):
    #     top=(n // 11)+1
    ready=False
    prim=[2,3,5,7,11,13,17,19,23,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,139,149,151,157,163,167,173,179,181]
    tamaño=len(prim)
    top=(n//2)+1
    k=0
    # este ciclo toma al numero y busca el menor valor primo divisible para obtener un rango de divisores y lo almacena en TOP
    while not ready and k<tamaño:
        if ((n % prim[k])==0):
            top=(n//prim[k])+1
            ready=True
        k=k+1
        
    
    for i in range(1,top):
        if ((n%i)==0):
            sum=sum+i
    return sum


@delta_time('Grupo 5')
def amigos(n):
    # amigos() compara desde el 220 hasta n
    # si encontró el par amigo [a,b] siendo siempre a<b
    # b se guardará en founded y la próxima vez no se analizará b
    # siempre se verifica que dado un numero i y la sumatoria de sus divisore i que z>i en caso contrario se descarta i
    founded=[]
    amigos=[]
    for i in range(220,n):
        if not(i in founded):
            x=divisores(i)
            if(x>i):
                y=divisores(x)
                if (i!=x) and (i==y):
                    amigos.append([i,x])
                    founded.append(x)
    return amigos
    
print(amigos(10000))

# @delta_time('Grupo 5')
# def sumatoria1(n):
#     for i in range(220,n+1):
#         divisores(i)


# sumatoria1(10000)
# print(divisores(9973))

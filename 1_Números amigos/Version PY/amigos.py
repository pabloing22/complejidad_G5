from decorators import delta_time


def divisores(n):
    sum=0
    top=0
    if(n % 2==0):
        top=(n // 2)+1
    elif(n % 3 == 0):
        top=(n // 3)+1
    elif (n % 5 == 0):
        top=(n // 5)+1
    elif (n % 7 == 0):
        top=(n // 7)+1
    elif (n % 11 == 0):
        top=(n // 11)+1
    else: 
        top=(n // 2)+1
    
    for i in range(1,top):
        if ((n%i)==0):
            sum=sum+i
    return sum


@delta_time('Grupo 5')
def amigos(n):
    founded=[]
    amigos=[]
    for i in range(219,n):
        if not(i in founded):
            x=divisores(i)
            if not(x in founded):
                y=divisores(x)
                if (i!=x) and (i==y):
                    amigos.append([i,x])
                    founded.append(x)
    return amigos
    
print(amigos(10000))

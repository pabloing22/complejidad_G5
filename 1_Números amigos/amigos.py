def divisores(nro):
    sumdiv=0
    max=nro
    if(max>50):
        if(nro%2==0):
            max=(nro//2)+1
        elif(nro%3==0):
            max = (nro // 3) + 1
        elif(nro%5==0):
            max = (nro // 5) + 1
        elif(nro%7==0):
            max = (nro // 7) + 1
        elif(nro%11==0):
            max = (nro // 11) + 1

    for (index,i) in enumerate(range(1,max)):
        if(nro%i==0):
            sumdiv=sumdiv+i
    return sumdiv


n=10000
def amigos(n):

    list=[]
    x=0
    y=0

    for j in range(220,n):
        a=j
        x=divisores(a)
        b=x
        if(a>b):
            y=divisores(b)
        if(a==y):
            list.append([b,a])
        x=0
        y=0
    return list

print(amigos(n))
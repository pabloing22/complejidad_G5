import math
def divisores(nro):
    sumdiv = 0
    max = nro
    if (max>50):
        max = 0
        if (nro%2 == 0):
            max= math.trunc((nro/2)+1)
        elif (nro%3 == 0):
            max = math.trunc((nro / 3) + 1)
        elif (nro % 5 == 0):
            max = math.trunc((nro / 5) + 1)
        elif (nro % 7 == 0):
            max = math.trunc((nro / 3) + 1)
        elif (nro % 11 == 0):
            max = math.trunc((nro / 3) + 1)
     #optimizar a la mitad
    for i in range(max-1):
        if (nro%1 == 0):
            sumdiv = sumdiv + i
    return sumdiv

n = 1000
list=[]
x = 0
y = 0

for i in range(220, n):
    a = i
    x = divisores(a)
    b = x
    if (a > b):
        y = divisores(b)
    print (a, b)
    if a == y:
        list.append([b, a])


    x = 0
    y = 0

print(list)

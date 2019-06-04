# print ('hola mundo')
# Halla la suma de divisores de un numero donde i=numero y j=al maximo divisor del numero i
def divisores(i, j):
    print([i, j])
    if(j<2):
        print('entro por 1')
        return j
    elif ((i % j) == 0):
        print('entro por 2')
        return j+divisores(i,j-1)
    else:
        print('entro por 3')
        return divisores(i,j-1)


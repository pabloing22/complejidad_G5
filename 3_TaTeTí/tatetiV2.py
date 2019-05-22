import os
from random import randrange
linea = [" ", " ", " "]
linea1 = [" ", " ", " "]
linea2 = [" ", " ", " "]
cuadrantes = [[0,1,2],[3,4,5],[6,7,8]]
pjugador = "X" #hay problemas en que si dejo esto en vacio, en la cuadrilla no se asigna nada en la pos que elige el jugador
pcompu = "O"
cuadrantes.append(linea)
cuadrantes.append(linea1)
cuadrantes.append(linea2)
etapa = 0
fila = 0
m = 0
def imprimirPantalla(cuadrantes):
    print((cuadrantes[0])[0], "|", (cuadrantes[0])[1], "|", (cuadrantes[0])[2])
    print("---------")
    print((cuadrantes[1])[0], "|", (cuadrantes[1])[1], "|", (cuadrantes[1])[2])
    print("---------")
    print((cuadrantes[2])[0], "|", (cuadrantes[2])[1], "|", (cuadrantes[2])[2])



def asignarpiezas():
    c = input('Seleccione su pieza (X o O) \n')
    pjugador = c
    

def ingreseNumero():
    print("ingrese posición")
    x = int(input("posicion x: "))
    y = int(input("posicion y: "))
    if(cuadrantes[x][y]!="X") and (cuadrantes[x][y]!="O"):
        cuadrantes[x][y] = pjugador
    else:
        print('posicion invalida, la casilla esta ocupada o ingreso numeros invalidos ')
        ingreseNumero()



def VueltaAtras(etapa,cuadrantes):
    for m in [0,1,2]:
        if(Valido(m,etapa,cuadrantes)==True):
            cuadrantes[m][etapa] = pcompu
            if etapa == 2:
                imprimirPantalla()
            else:
                VueltaAtras(etapa+1,cuadrantes)



def Valido(m,etapa,cuadrantes):

    for i in [0,1,2]:
        if cuadrantes[m][i]=="X" or cuadrantes[m][i]=="O":
            return False

    for j in [0,1,2]:
        if cuadrantes[m][j]=="X" or cuadrantes[m][j]=="O":
            return False

    return True


def esquinaLibre(fila,etapa,cuadrantes):
    if(cuadrantes[fila][etapa]!="O")and(cuadrantes[fila][etapa]!="X"):
        return True
    else:
        etapa = etapa + 2
        if(etapa > 2):
            etapa = 0
            fila = fila + 2

        esquinaLibre(fila,etapa,cuadrantes)




def juegaMaquina():
    if(cuadrantes[1][1]!="X")and(cuadrantes[1][1]!="O"): #Pregunta si esta libre el centro
        cuadrantes[1][1]=pcompu
        imprimirPantalla(cuadrantes)
    else:
        if(esquinaLibre(fila,etapa,cuadrantes)==True): #Pregunta si alguna esquina está libre
            cuadrantes[fila][etapa] = pcompu
        else:
            VueltaAtras(etapa,cuadrantes)
            Valido(m,etapa,cuadrantes)




njugadas = 5
asignarpiezas()
imprimirPantalla(cuadrantes)
while njugadas > 0:
    ingreseNumero()
    os.system('cls')
    imprimirPantalla(cuadrantes)
    juegaMaquina()
    njugadas = njugadas-1


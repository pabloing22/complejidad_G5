import os
from random import randrange
import random
cuadrantes = [[0,1,2],[3,4,5],[6,7,8]]
esquinas = [0,2,6,8]
medios = [1,3,5,7]
pjugador = "X" #hay problemas en que si dejo esto en vacio, en la cuadrilla no se asigna nada en la pos que elige el jugador
pcompu = "O"
etapa = 0
pieza=None
fila = 0
m = 0

def imprimirPantalla(cuadrantes):
    print((cuadrantes[0])[0], "|", (cuadrantes[0])[1], "|", (cuadrantes[0])[2])
    print("---------")
    print((cuadrantes[1])[0], "|", (cuadrantes[1])[1], "|", (cuadrantes[1])[2])
    print("---------")
    print((cuadrantes[2])[0], "|", (cuadrantes[2])[1], "|", (cuadrantes[2])[2])
    print('--------------------------------------------------------------------')



def asignarpiezas():
    c = input('Seleccione su pieza (X o O) \n')
    pjugador = c
    
def descartarPosicion(x,y): #Elimina posiciones disponibles
	#Descartando esquinas
	if(x==0):
		if(y==0):
			esquinas.remove(0)
		elif y==2:
			esquinas.remove(2)
	elif x==2:
		if(y==0):
			esquinas.remove(6)
		elif y==2:
			esquinas.remove(8)
	#Descartando medios
	if(x==1):
		if y==0:
			medios.remove(3)
		elif y==2:
			medios.remove(5)
	else:
		if(y==1):
			if(x==0):
				medios.remove(1)
			elif x==2:
				medios.remove(7)

def ingreseNumero():
    print("ingrese posición")
    x = int(input("posicion x: "))
    y = int(input("posicion y: "))
    if(cuadrantes[x][y]!="X") and (cuadrantes[x][y]!="O"):
        cuadrantes[x][y] = pjugador
        descartarPosicion(x,y)
    else:
        print('posicion invalida, la casilla esta ocupada o ingreso numeros invalidos ')
        ingreseNumero()


def esquinaLibre(cuadrantes): #Pregunta si hay una esquina libre
	if esquinas:
		return True
	else:
		return False

def taparColumna(cuadrantes,x,z): #Tapa la jugada en la columna
	for x in[0,1,2]:
		if(cuadrantes[x][z]!="X")and(cuadrantes[x][z]!="O"):
			cuadrantes[x][z]=pcompu
			descartarPosicion(x,z)

def ganaJugador(cuadrantes): #Verifica si el jugador puede ganar en la próxima jugada, es medio complicado de explicar porque tanto anidamiento de condiciones, pero tiene su razón
    #Control de filas
    if((cuadrantes[0][0]==cuadrantes[0][1])and cuadrantes[0][0]=="X"  and cuadrantes[0][2]!="O")or((cuadrantes[0][0]==cuadrantes[0][2])and cuadrantes[0][0]=="X" and cuadrantes[0][1]!="O")or((cuadrantes[0][1]==cuadrantes[0][2]) and cuadrantes[0][1]=="X" and cuadrantes[0][0]!="O"):
        taparFila(0,cuadrantes,0)
        return True
    if((cuadrantes[1][0]==cuadrantes[1][1])and cuadrantes[1][0]=="X" and cuadrantes[1][2]!="O")or((cuadrantes[1][0]==cuadrantes[1][2])and cuadrantes[1][0]=="X" and cuadrantes[1][1]!="O")or((cuadrantes[1][1]==cuadrantes[1][2]) and cuadrantes[1][1]=="X" and cuadrantes[1][0]!="O"):
    	taparFila(1,cuadrantes,0)
    	return True
    if(cuadrantes[2][0]==cuadrantes[2][1]and cuadrantes[2][0]=="X"  and cuadrantes[2][2]!="O")or(cuadrantes[2][0]==cuadrantes[2][2]and cuadrantes[2][0]=="X"  and cuadrantes[2][1]!="O")or(cuadrantes[2][1]==cuadrantes[2][2] and cuadrantes[2][1]=="X" and cuadrantes[2][0]!="O"):
    	taparFila(2,cuadrantes,0)
    	return True
    #Control de columnas
    if(cuadrantes[0][0]==cuadrantes[1][0]and cuadrantes[0][0]=="X"  and cuadrantes[2][0]!="O")or(cuadrantes[0][0]==cuadrantes[2][0]and cuadrantes[0][0]=="X" and cuadrantes[1][0]!="O")or(cuadrantes[1][0]==cuadrantes[2][0] and cuadrantes[1][0]=="X"and cuadrantes[0][0]!="O"):
    	taparColumna(cuadrantes,0,0)
    	return True
    if(cuadrantes[0][1]==cuadrantes[1][1]and cuadrantes[0][1]=="X" and cuadrantes[2][1]!="O")or(cuadrantes[0][1]==cuadrantes[2][1]and cuadrantes[0][1]=="X" and cuadrantes[1][1]!="O")or(cuadrantes[1][1]==cuadrantes[2][1] and cuadrantes[1][1]=="X" and cuadrantes[0][1]!="O"):
    	taparColumna(cuadrantes,0,1)
    	return True
    if(cuadrantes[0][2]==cuadrantes[1][2]and cuadrantes[0][2]=="X"  and cuadrantes[2][2]!="O")or(cuadrantes[0][2]==cuadrantes[2][2]and cuadrantes[0][2]=="X"  and cuadrantes[1][1]!="O")or(cuadrantes[1][2]==cuadrantes[2][2]and cuadrantes[2][2]=="X"and cuadrantes[0][2]!="O"):
    	taparColumna(cuadrantes,0,2)
    	return True
    #Control de diagonales
    if(cuadrantes[0][0]==cuadrantes[1][1]and cuadrantes[0][0]=="X"  and cuadrantes[2][2]!="O")or(cuadrantes[0][0]==cuadrantes[2][2]and cuadrantes[2][2]=="X"  and cuadrantes[1][1]!="O")or(cuadrantes[1][1]==cuadrantes[2][2]and cuadrantes[2][2]=="X"and cuadrantes[0][0]!="O"):
    	taparDiagonal(cuadrantes,1,1)
    	return True
    if(cuadrantes[0][2]==cuadrantes[1][1]and cuadrantes[0][2]=="X" and cuadrantes[2][0]!="O")or(cuadrantes[0][2]==cuadrantes[2][0]and cuadrantes[2][0]=="X"  and cuadrantes[1][1]!="O")or(cuadrantes[1][1]==cuadrantes[2][0]and cuadrantes[2][0]=="X"and cuadrantes[0][2]!="O"):
    	taparDiagonal(cuadrantes,1,1)
    	return True
    return False

def taparDiagonal(cuadrantes,m,n): #Tapa jugadas en la diagonal
	if(cuadrantes[0][0]==cuadrantes[m][n]):
		cuadrantes[m+1][n+1]=pcompu
		esquinas.remove(8)
	elif cuadrantes[m][n]==cuadrantes[m+1][n+1]:
		cuadrantes[0][0]=pcompu
		esquinas.remove(0)
	elif cuadrantes[m][n]==cuadrantes[m-1][n+1]:
		cuadrantes[2][0]=pcompu
		esquinas.remove(6)
	elif cuadrantes[m][n]==cuadrantes[m+1][n-1]:
		cuadrantes[0][2]=pcompu
		esquinas.remove(2)

def taparFila(j,cuadrantes,k): #Tapa jugadas en las filas
    if(cuadrantes[j][k]!="X")and(cuadrantes[j][k]!="O"):
        cuadrantes[j][k]=pcompu
    else:
        k = k + 1
        if(k <= 2):
            taparFila(j,cuadrantes,k)
        else:
        	k = 0
        	j = j + 1

 
def lugarMedio(cuadrantes): #Pregunta si hay lugar en los medios
	if medios:
		return True
	else:
		return False

def puedoGanar(cuadrantes): #Tiene la misma funcion que la funcion ganarJugador, la maquina ve si puede ganar en la proxima jugada
	#Control de filas
    if((cuadrantes[0][0]==cuadrantes[0][1])and cuadrantes[0][0]=="O"  and cuadrantes[0][2]!="X")or((cuadrantes[0][0]==cuadrantes[0][2])and cuadrantes[0][0]=="O" and cuadrantes[0][1]!="O")or((cuadrantes[0][1]==cuadrantes[0][2]) and cuadrantes[0][1]=="O" and cuadrantes[0][0]!="X"):
        Victoria(cuadrantes,0,0)
        return True
    if((cuadrantes[1][0]==cuadrantes[1][1])and cuadrantes[1][0]=="O" and cuadrantes[1][2]!="O")or((cuadrantes[1][0]==cuadrantes[1][2])and cuadrantes[1][0]=="O" and cuadrantes[1][1]!="O")or((cuadrantes[1][1]==cuadrantes[1][2]) and cuadrantes[1][1]=="O" and cuadrantes[1][0]!="X"):
    	Victoria(cuadrantes,1,0)
    	return True
    if(cuadrantes[2][0]==cuadrantes[2][1]and cuadrantes[2][0]=="O"  and cuadrantes[2][2]!="O")or(cuadrantes[2][0]==cuadrantes[2][2]and cuadrantes[2][0]=="O"  and cuadrantes[2][1]!="O")or(cuadrantes[2][1]==cuadrantes[2][2] and cuadrantes[2][1]=="O" and cuadrantes[2][0]!="X"):
    	Victoria(cuadrantes,2,0)
    	return True
    #Control de columnas
    if(cuadrantes[0][0]==cuadrantes[1][0]and cuadrantes[0][0]=="O"  and cuadrantes[2][0]!="O")or(cuadrantes[0][0]==cuadrantes[2][0]and cuadrantes[0][0]=="O" and cuadrantes[1][0]!="O")or(cuadrantes[1][0]==cuadrantes[2][0] and cuadrantes[1][0]=="O"and cuadrantes[0][0]!="X"):
    	Victoria(cuadrantes,0,0)
    	return True
    if(cuadrantes[0][1]==cuadrantes[1][1]and cuadrantes[0][1]=="O" and cuadrantes[2][1]!="O")or(cuadrantes[0][1]==cuadrantes[2][1]and cuadrantes[0][1]=="O" and cuadrantes[1][1]!="O")or(cuadrantes[1][1]==cuadrantes[2][1] and cuadrantes[1][1]=="O" and cuadrantes[0][1]!="X"):
    	Victoria(cuadrantes,0,1)
    	return True
    if(cuadrantes[0][2]==cuadrantes[1][2]and cuadrantes[0][2]=="O"  and cuadrantes[2][2]!="O")or(cuadrantes[0][2]==cuadrantes[2][2]and cuadrantes[0][2]=="O"  and cuadrantes[1][1]!="O")or(cuadrantes[1][2]==cuadrantes[2][2]and cuadrantes[2][2]=="O"and cuadrantes[0][2]!="X"):
    	Victoria(cuadrantes,0,2)
    	return True
    #Control de diagonales
    if(cuadrantes[0][0]==cuadrantes[1][1]and cuadrantes[0][0]=="O"  and cuadrantes[2][2]!="O")or(cuadrantes[0][0]==cuadrantes[2][2]and cuadrantes[2][2]=="O"  and cuadrantes[1][1]!="O")or(cuadrantes[1][1]==cuadrantes[2][2]and cuadrantes[2][2]=="O"and cuadrantes[0][0]!="X"):
    	Victoria(cuadrantes,1,1)
    	return True
    if(cuadrantes[0][2]==cuadrantes[1][1]and cuadrantes[0][2]=="O" and cuadrantes[2][0]!="O")or(cuadrantes[0][2]==cuadrantes[2][0]and cuadrantes[2][0]=="O"  and cuadrantes[1][1]!="O")or(cuadrantes[1][1]==cuadrantes[2][0]and cuadrantes[2][0]=="O"and cuadrantes[0][2]!="X"):
    	Victoria(cuadrantes,1,1)
    	return True

def Victoria(cuadrantes,f,c): #Tecnicamente esta funcion hace que la maquina coloque su ultima ficha en la posicion que corresponde para ganar el duelo
	if(cuadrantes[f][c]!="X")and(cuadrantes[f][c]!="O"):
		cuadrantes[f][c]=pcompu
	else:
		c=c+1
		if(c>2):
			c=0
			f=f+1
		Victoria(cuadrantes,f,c)



def juegaMaquina():
	
    if(ganaJugador(cuadrantes)==False):
        if(cuadrantes[1][1]!="X")and(cuadrantes[1][1]!="O"): #Pregunta si esta libre el centro
            cuadrantes[1][1]=pcompu
        else:
            if(esquinaLibre(cuadrantes)==True): #Pregunta si alguna esquina está libre
            	m = random.choice(esquinas) #Hace una eleccion al azar entre las esquinas disponibles
            	if(m==0):
            		cuadrantes[0][0]=pcompu
            	elif m==2:
            		cuadrantes[0][2]=pcompu
            	elif m==6:
            		cuadrantes[2][0]=pcompu
            	elif m==8:
            		cuadrantes[2][2]=pcompu
            	esquinas.remove(m) #Y aca elimina de la lista de esquinas, la ubicacion elegida
            else:
            	if(lugarMedio(cuadrantes)==True): #ídem que en el caso de las esquinas
            		m = random.choice(medios)
            		if(m==1):
            			cuadrantes[0][1]=pcompu
            		elif m==3:
            			cuadrantes[1][0]=pcompu
            		elif m==5:
            			cuadrantes[1][2]=pcompu
            		elif m==7:
            			cuadrantes[2][1]=pcompu
            		medios.remove(m)
    else:
    	pass

def hayLugar(a,b): #Aca pregunta si hay lugares en las esquinas o en los medios
	if a and b:
		return True
	else:
		return False
def ganoAlguien(): #Va a retornar un True si gano alguien
	return((cuadrantes[0][0]==pjugador)and(cuadrantes[0][1]==pjugador)and(cuadrantes[0][2]==pjugador)or(cuadrantes[1][0]==pjugador)and(cuadrantes[1][1]==pjugador)and(cuadrantes[1][2]==pjugador)or
			(cuadrantes[2][0]==pjugador)and(cuadrantes[2][1]==pjugador)and(cuadrantes[2][2]==pjugador)or(cuadrantes[0][0]==pjugador)and(cuadrantes[1][0]==pjugador)and(cuadrantes[2][0]==pjugador)or
			(cuadrantes[0][1]==pjugador)and(cuadrantes[1][1]==pjugador)and(cuadrantes[2][1]==pjugador)or(cuadrantes[0][2]==pjugador)and(cuadrantes[1][2]==pjugador)and(cuadrantes[2][2]==pjugador)or
			(cuadrantes[0][0]==pjugador)and(cuadrantes[1][1]==pjugador)and(cuadrantes[2][2]==pjugador)or(cuadrantes[0][2]==pjugador)and(cuadrantes[1][1]==pjugador)and(cuadrantes[2][0]==pjugador))

	pieza = pjugador

	return((cuadrantes[0][0]==pcompu)and(cuadrantes[0][1]==pcompu)and(cuadrantes[0][2]==pcompu)or(cuadrantes[1][0]==pcompu)and(cuadrantes[1][1]==pcompu)and(cuadrantes[1][2]==pcompu)or
			(cuadrantes[2][0]==pcompu)and(cuadrantes[2][1]==pcompu)and(cuadrantes[2][2]==pcompu)or(cuadrantes[0][0]==pcompu)and(cuadrantes[1][0]==pcompu)and(cuadrantes[2][0]==pcompu)or
			(cuadrantes[0][1]==pcompu)and(cuadrantes[1][1]==pcompu)and(cuadrantes[2][1]==pcompu)or(cuadrantes[0][2]==pcompu)and(cuadrantes[1][2]==pcompu)and(cuadrantes[2][2]==pcompu)or
			(cuadrantes[0][0]==pcompu)and(cuadrantes[1][1]==pcompu)and(cuadrantes[2][2]==pcompu)or(cuadrantes[0][2]==pcompu)and(cuadrantes[1][1]==pcompu)and(cuadrantes[2][0]==pcompu))

	pieza = pcompu

asignarpiezas()
imprimirPantalla(cuadrantes)

while hayLugar(esquinas,medios)==True and ganoAlguien()==False: #Se ejecuta mientras el tablero NO este lleno y mientras no haya ganado alguien
    ingreseNumero()
    os.system('cls')
    juegaMaquina()
    imprimirPantalla(cuadrantes)
 

if(ganoAlguien()==False):
	print('<-- HAY EMPATE -->')
else:
	print('GANO ALGUIEN') #La idea en este sector es que muestre quien gano, aunque por la forma en que lo hice, creo que es medio dificil que alguien gane (o a lo sumo la PC) xD
	print(pieza)




    


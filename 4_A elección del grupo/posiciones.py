solucion=[['B2',3,2],['N3',1,1],['B1',1,3],['N4',0,3],['B3',3,1],['N2',1,2],['B2',1,0],['N3',3,3],\
          ['B1',0,2],['N4',4,1],['B3',2,0],['N2',2,3],['B2',2,1],['N3',2,2],['B3',4,2],['N2',0,1],\
          ['B2',0,3],['N3',4,0],['B4',2,1],['N1',2,2],['B1',2,0],['N4',2,3],['B4',3,0],['N1',1,3],\
          ['B3',3,3],['N2',1,0],['B3',0,0],['N2',4,3],['B1',1,1],['N4',3,2],['B4',1,2],['N1',3,1],\
          ['B1',0,2],['N4',4,1],['B4',0,1],['N1',4,2]]
blancas=(' B1 ',' B2 ',' B3 ',' B4 ')
negras=(' N1 ',' N2 ',' N3 ',' N4 ')
tablero=[[' N1 ',' N2 ',' N3 ',' N4 '],['    ','    ','    ','    '],['    ','    ','    ','    '],['    ','    ','    ','    '],[' B1 ',' B2 ',' B3 ',' B4 ']]
tablero_prueba=[[' N1 ','    ',' B1 ','    '],['    ','    ','    ','    '],[' B3 ',' B2 ','    ',' N2 '],['    ','    ','    ',' N3 '],['    ',' N4 ','    ',' B4 ']]

def solucion_encontrada(tablero):
	solucion=True
	for j in range(4):
		if tablero[0][j] not in blancas:
			return False
	for i in range(4):
		if tablero[4][j] not in negras:
			return False
	return solucion

def actualizar_tablero(tablero,movimiento):
	ficha_a_mover=movimiento[0]
	for i in tablero:
		cont=0
		for j in i:
			if j==ficha_a_mover:
				i[cont]='    '	
			cont=cont+1
	tablero[movimiento[1]][movimiento[2]]=ficha_a_mover
	return tablero

def mostrar_tablero(tablero):
	fila=0
	print('\n\n  0    1    2    3 ')
	print('---------------------')
	for i in tablero:
		for j in i:
			print('|',end='')
			print(j,end='')
		print('| ',fila);fila=fila+1
		print('---------------------')

#esta funcion es un embole, pone un "cursor" en la posicon del alfil acutual y hace un recorrido en diagonal
#lo hace en cuatro sentidos, arriba a la izquiera, arriba a la derecha, abajo a la izquierda y
#abajo a la derecha. A medida que encuetra una posicion libre en tales diagonales la agrega a la 
#lista de salida, si en algun momento choca con algun otro alfil sale del bucle y sigue con la otra
#diagonal 

def diagonal(tablero,ficha):	
	coordenadas=obtener_coordenadas(tablero,ficha)
	resultado=[]
	x=coordenadas[0]
	y=coordenadas[1]
	x=x+1;y=y+1
	while -1<x<5 and -1<y<4:
		if ((tablero[x][y]) in blancas) or ((tablero[x][y]) in negras):
			break
		resultado.append([x,y])
		x=x+1;y=y+1
	x=coordenadas[0]
	y=coordenadas[1]
	x=x-1;y=y-1
	while -1<x<5 and -1<y<4:
		if ((tablero[x][y]) in blancas) or ((tablero[x][y]) in negras):
			break		
		resultado.append([x,y])
		x=x-1;y=y-1
	x=coordenadas[0]
	y=coordenadas[1]
	x=x+1;y=y-1
	while -1<x<5 and -1<y<4:
		if ((tablero[x][y]) in blancas) or ((tablero[x][y]) in negras):
			break		
		resultado.append([x,y])
		x=x+1;y=y-1
	x=coordenadas[0]
	y=coordenadas[1]
	x=x-1;y=y+1
	while -1<x<5 and -1<y<4:
		if ((tablero[x][y]) in blancas) or ((tablero[x][y]) in negras):
			break		
		resultado.append([x,y])
		x=x-1;y=y+1
	return resultado

def obtener_coordenadas(tablero,ficha):
	fila=0
	for i in tablero:
		columna=0
		for j in i:
			if j==ficha:
				coordenadas=(fila,columna)#devuelve la poscion cuando encuentra una coincidencia 
				return coordenadas
			columna=columna+1
		fila=fila+1

def posibles_movimientos(tablero,ficha):
	combinaciones=diagonal(tablero,ficha)#busco todas las posiciones que estan en la misma diagonal que el alfil actual
	resultado=list()
	if ficha in blancas:
		color_opuesto=negras
	else:
		color_opuesto=blancas
	for i in combinaciones:
		band=True
		for j in color_opuesto:
			if misma_diagonal(tablero,i,j):#si hay algun alfil del equipo contrario en esa diagonal la elimina de la lista
				band=False
		if band:
			resultado.append(i)
	return resultado

def misma_diagonal(tablero,ficha1,ficha2):
	if isinstance(ficha1,str):
		cord1=obtener_coordenadas(tablero,ficha1)
	else:
		cord1=ficha1
	if isinstance(ficha2,str):
		cord2=obtener_coordenadas(tablero,ficha2)
	else:
		cord2=ficha2
	if (abs(cord1[0]-cord2[0])) == (abs(cord1[1]-cord2[1])):
		return True
	else:
		return False

mostrar_tablero(tablero_prueba)

for b in blancas:
	print('Posibles posibles_movimientos de ',b,':\n')
	print(posibles_movimientos(tablero_prueba,b))
	print()



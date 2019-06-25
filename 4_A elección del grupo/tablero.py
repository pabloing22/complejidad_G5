solucion=[['B2',3,2],['N3',1,1],['B1',1,3],['N4',0,3],['B3',3,1],['N2',1,2],['B2',1,0],['N3',3,3],\
          ['B1',0,2],['N4',4,1],['B3',2,0],['N2',2,3],['B2',2,1],['N3',2,2],['B3',4,2],['N2',0,1],\
          ['B2',0,3],['N3',4,0],['B4',2,1],['N1',2,2],['B1',2,0],['N4',2,3],['B4',3,0],['N1',1,3],\
          ['B3',3,3],['N2',1,0],['B3',0,0],['N2',4,3],['B1',1,1],['N4',3,2],['B4',1,2],['N1',3,1],\
          ['B1',0,2],['N4',4,1],['B4',0,1],['N1',4,2]]

#cada subarreglo del arreglo "solucion" contiene el alfil que se va a mover y a que posicion se movera

def mostrar_tablero(tablero):
	print('\n\n---------------------')
	for i in tablero:
		for j in i:
			print('|',end='')
			print(j,end='')
		print('|')
		print('---------------------')

def actualizar_tablero(tablero,movimiento):
	ficha_a_mover=(' ')+movimiento[0]+(' ')
	for i in tablero:#este bucle busca el alfil que se quiere mover para borrarlo para que al ponerlo en el tablero no se lo escriba dos veces
		cont=0
		for j in i:
			if j==ficha_a_mover:
				i[cont]='    '#deja vacia la antigua posicion del alfil  
			cont=cont+1
	tablero[movimiento[1]][movimiento[2]]=ficha_a_mover#una vez borrada la posicion vieja, pongo el alfil en la nueva posicion
	mostrar_tablero(tablero)#hecho el movimiento del alfil muestro como quedo el tablero 


tablero=[[' N1 ',' N2 ',' N3 ',' N4 '],['    ','    ','    ','    '],['    ','    ','    ','    '],['    ','    ','    ','    '],[' B1 ',' B2 ',' B3 ',' B4 ']]

#cada subarreglo del arreglo es una fila del tablero

for i in solucion:
	actualizar_tablero(tablero,i)
	

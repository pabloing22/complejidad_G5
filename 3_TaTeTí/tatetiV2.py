from math import inf as infinity
from random import choice
import platform
import time
from os import system
import os
HUMAN = -1
COMP = +1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

def evaluar(estado): #Funcion heuristica
	if ganador(estado,COMP):
		puntaje = +1
	elif ganador(estado,HUMAN):
		puntaje=-1
	else:
		puntaje = 0
	return puntaje

def ganador(estado,jugador):
	win_state = [
        [estado[0][0], estado[0][1], estado[0][2]],
        [estado[1][0], estado[1][1], estado[1][2]],
        [estado[2][0], estado[2][1], estado[2][2]],
        [estado[0][0], estado[1][0], estado[2][0]],
        [estado[0][1], estado[1][1], estado[2][1]],
        [estado[0][2], estado[1][2], estado[2][2]],
        [estado[0][0], estado[1][1], estado[2][2]],
        [estado[2][0], estado[1][1], estado[0][2]],
    ]
	if [jugador, jugador, jugador] in win_state:
		return True
	else:
		return False

def derrota(estado):
	return ganador(estado,HUMAN) or ganador(estado,COMP)

def celdas_vacias(estado):
	celdas = []

	for x, row in enumerate(estado):
		for y, cell in enumerate(row):
			if cell == 0:
				celdas.append([x, y])

	return celdas

def validar_movimiento(x,y):
	if [x, y] in celdas_vacias(board):
		return True
	else:
		return False

def tomarMovimiento(x,y,jugador):
	if validar_movimiento(x, y):
		board[x][y] = jugador
		return True
	else:
		return False

def minimax(estado, profundidad, jugador):
    if jugador == COMP:
        mejor = [-1, -1, -infinity]
    else:
        mejor = [-1, -1, +infinity]

    if profundidad == 0 or derrota(estado):
        puntaje = evaluar(estado)
        return [-1, -1, puntaje]

    for cell in celdas_vacias(estado):
        x, y = cell[0], cell[1]
        estado[x][y] = jugador
        puntaje = minimax(estado, profundidad - 1, -jugador)
        estado[x][y] = 0
        puntaje[0], puntaje[1] = x, y

        if jugador == COMP:
            if puntaje[2] > mejor[2]:
                mejor = puntaje  # max value
        else:
            if puntaje[2] < mejor[2]:
               mejor = puntaje  # min value

    return mejor

def imprimir(estado, pcompu, phumano):
    chars = {
        -1: phumano,
        +1: pcompu,
        0: ' '
    }
    str_line = '---------------'

    print('\n' + str_line)
    for row in estado:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)

def juegaPC(pcompu, phumano):
  
    profundidad = len(celdas_vacias(board))
    if profundidad == 0 or derrota(board):
        return


    print('Turno del PC')
    imprimir(board, pcompu, phumano)

    if profundidad == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        movimiento = minimax(board, profundidad, COMP)
        x, y = movimiento[0], movimiento[1]

    tomarMovimiento(x, y, COMP)
    time.sleep(1)

def juegaHumano(pcompu, phumano):

    profundidad = len(celdas_vacias(board))
    if profundidad == 0 or derrota(board):
        return

    # Dictionary of valid moves
    movimiento = -1
    celdas = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    print('Turno del Jugador (X)')
    imprimir(board, pcompu, phumano)
    movimiento = int(input('Digite un numero (1--9)\n'))
    while(movimiento<1 or movimiento > 9):
    	imprimir(board,pcompu,phumano)
    	print('Casilla invalida')
    	movimiento = int(input('Digite un numero (1--9)\n'))


    coord = celdas[movimiento]
    can_move = tomarMovimiento(coord[0], coord[1], HUMAN)

def principal():
    phumano = 'X'  # X or O
    pcompu = 'O'  # X or O
    first = ''  # if human is the first

    # Main loop of this game
    while len(celdas_vacias(board)) > 0 and not derrota(board):  
        juegaHumano(pcompu, phumano)
        os.system('cls')
        juegaPC(pcompu, phumano)

    # Game over message
    if ganador(board, HUMAN):
        
        print('Turno del jugador (X)')
        imprimir(board, pcompu, phumano)
        print('HAS GANADO!')
    elif ganador(board, COMP):
       
        print('Turno del PC')
        imprimir(board, pcompu, phumano)
        print('HAS PERDIDO!')
    else:
    	imprimir(board, pcompu, phumano)
    	print('EMPATE')

    exit()


principal()























    


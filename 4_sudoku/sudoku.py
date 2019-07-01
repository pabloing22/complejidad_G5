# board = [
#     [0,5,4,6,0,0,0,0,0],
#     [0,0,0,0,7,0,9,0,0],
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,0,8,0,0,3,0,6],
#     [0,0,0,0,0,0,0,0,8],
#     [7,6,0,0,0,0,0,0,5],
#     [0,0,0,0,5,0,0,0,2],
#     [9,0,0,2,0,0,0,0,0],
#     [3,0,1,0,0,0,0,7,0]
# ]
# board = [
#     [0,5,4,6,0,0],
#     [0,0,0,0,7,0],
#     [0,0,0,0,0,0],
#     [0,0,0,8,0,0],
#     [0,0,0,0,0,0],
#     [7,6,0,0,0,0],
#     [0,0,0,0,5,0],
#     [9,0,0,2,0,0],
#     [3,0,1,0,0,0]
# ]
board = [
    [0,2,0],
    [3,0,0],
    [0,0,1]
]

# def sudoku(board):


def renderizar(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


# busca y retorna la primera posición donde encuentre un numero 0
def buscar(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                return (i, j)
    return None

def solucion(board, n, pos):

    # pos[0] contiene a row
    # pos[1] contiene a col
 
    # verificamos fila
    for i in range(len(board[0])):
        # board[row][i] va recorriendo la fila donde se encuentra el valor a rellenar
        # pos
        if board[pos[0]][i] == n and pos[1] != i:
            return False
    
    # verificamos columna
    for i in range(len(board)):
        if board[i][pos[1]] == n and pos[0] != i:
            return False
    
    # verificamos por caja
    # box_x=pos[1]//3
    # box_y=pos[0]//3

    # for i in range(box_y*3, box_y*3+3):
    #     for j in range(box_x*3, box_x *3+3):
    #         if board[i][j] == n and (i, j) != pos:
    #             return False
    
    return True

def sudoku(board):

    vacio=buscar(board)
    # vacio contendrá una dupla con las coordenadas del primer 0 que encuentre
    if not (vacio):
        # si vacio es nulo significa que no hay casillas qué completar
        return True
    else:
        # en caso contrario, desmenuza vacio en dos variables: row contrendrá la coordenada en x y col la coordenada en i
        row, col = vacio
    
    # el for principal recorre todos los números posibles para rellenar la casilla de posición (row, col) con todos sus posibles valores del 1 al 9.
    for i in range(1,len(board)+1):

        if solucion(board, i, (row, col)): #sí es válido el número i, en la posición (row,col) entonces

            board[row][col]=i # al tablero en la posición (row,col) le asigno el número i
            
            #RECURSIÓOOOONN
            if sudoku(board):
                return True

            board[row][col] = 0


renderizar(board)
sudoku(board)
print("=========================")
print("=========================")
renderizar(board)

# print(buscar(board))
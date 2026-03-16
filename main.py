#Sudoku erster Versuch

grid = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]

def print_grid(board):
    for row in range(9): 
        if row % 3 == 0 and row != 0: 
            print("-------------------------")
        for col in range(9): 
            if col % 3 == 0: 
                print("|", end=" ")
            print(board[row][col], end=" ")
        print("|", end=" ")
        print()



def allowed(board, zeile, spalte, zahl):
    for i in range(9):                                                  #Zeile überprüfen
       if board[zeile][i] == zahl: 
           return False

    for j in range(9):                                                  #Spalte überprüfen
        if board[j][spalte] == zahl:
            return False
        
    m = (zeile // 3) * 3                                                #Block überprüfen
    n = (spalte // 3) * 3

    for i in range(3): 
        for j in range(3):
            if board[m + i][n + j] == zahl: 
                return False
    return True





print_grid(grid) 
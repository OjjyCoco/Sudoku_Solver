import numpy as np 

SudokuMatrice = [[0,0,7,0,2,0,1,0,0],
                 [0,0,8,0,0,9,0,7,6],
                 [0,0,2,6,7,0,0,4,0], 
                 [0,0,5,0,9,0,3,6,0], 
                 [9,3,0,0,0,0,0,0,0], 
                 [0,1,0,0,0,0,0,9,7], 
                 [5,0,3,0,0,0,0,0,0], 
                 [0,0,0,8,0,0,5,1,0], 
                 [0,7,0,0,0,3,0,0,0]]

print(np.matrix(SudokuMatrice))

def check(x, y, n):

    if SudokuMatrice[y][x] != 0:
        return False

    for nbr in np.array(SudokuMatrice)[:,x]: # test les colonnes
        if nbr == n:
            return False
    for nbr in SudokuMatrice[y]: # test les lignes
        if nbr == n:
            return False

    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0,3): # test les carrés
        for j in range(0,3):
            if n == SudokuMatrice[y0 + i][x0 + j]:
                return False

    return True

def SudokuSolver():
    for y in range(9):
        for x in range(9):
            if SudokuMatrice[y][x] == 0:
                for n in range(1, 10):
                    if check(x, y, n):
                        SudokuMatrice[y][x] = n
                        SudokuSolver()
                        SudokuMatrice[y][x] = 0
                return
    print("\n Solution : \n",np.matrix(SudokuMatrice))


SudokuSolver()
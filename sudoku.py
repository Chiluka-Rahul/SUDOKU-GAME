import numpy as np
puzzle=[
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,0,0]
    ]

def possible(row,col,num):
    global puzzle
    for i in range(0,9):
        if puzzle[row][i]==num:
            return False
    for i in range(0,9):
        if puzzle[i][col]==num:
            return False
    x=(col // 3) * 3 
    y=(row // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if puzzle[y+i][x+j] == num:
                return False
    return True
def solve():
    global puzzle
    for row in range(0,9):
        for col in range(0,9):
            if puzzle[row][col]==0:
                for num in range(1,10):
                    if possible(row,col,num):
                        puzzle[row][col]= num
                        solve()
                        puzzle[row][col]=0
                return 
    print(np.matrix(puzzle))
    input('Instead of this!')
solve()    
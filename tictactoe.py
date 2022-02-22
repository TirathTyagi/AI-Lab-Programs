from random import randint
def on_board(board, x, y):
    try:
        board[int(x)][int(y)]
    except IndexError:
        return False
    else:
        return True
def checkFull(curstate):
    elems = 0
    rows  = len(curstate)
    for i in range(rows):
        cols = len(curstate[i])
        for j in range(cols):
            if curstate[i][j] == 'X' or curstate[i][j] == 'O':
                elems = elems+1
    if elems == 9:
        return True
    else:
        return False
def checkRow(curstate):
    i = 0
    while i <3:
        countx = 0
        county = 0
        rows = len(curstate[i])
        for j in range(rows):
            if curstate[i][j] == 'X':
                countx = countx+1
            elif curstate[i][j] == 'O':
                county = county+1
        if countx == 3:
            print("WINNER: HUMAN!!!!!!!!!")
            return True
        elif county == 3:
            print("WINNER: MACHINE!!!!!!!!!")
            return True
        else:
            i = i+1
def checkCol(curstate):
    i = 0
    while i<3:
        countx = 0
        county = 0
        cols = len(curstate)
        for j in range(cols):
            if curstate[j][i] == 'X':
                countx = countx + 1
            elif curstate[j][i] == 'O':
                county = county + 1
        if countx == 3:
            print("WINNER: HUMAN!!!!!!!!!")
            return True
        elif county == 3:
            print("WINNER: MACHINE!!!!!!!!!")
            return True
        else:
            i= i+1
    return False
def checkDiagonals(curstate):
    cols = len(curstate)
    countx = 0
    county = 0
    for i in range(cols):
        if curstate[i][i] == 'X':
            countx = countx+1
        elif curstate[i][i] == 'O':
            county = county+1
    if countx == 3:
        print("WINNER: HUMAN!!!!!!!!!")
        return True
    elif county == 3:
        print("WINNER: MACHINE!!!!!!!!!")
        return True
    else:
        if curstate[0][2] == curstate[1][1] == curstate[2][0] == 'X':
            print("WINNER: HUMAN!!!!!!!!!")
            return True
        elif curstate[0][2] == curstate[1][1] == curstate[2][0] == 'O':
            print("WINNER: MACHINE!!!!!!!!!")
            return True
        else:
            return False
def checkWin(curstate):
    if checkRow(curstate) or checkCol(curstate) or checkDiagonals(curstate):
        return True
    else:
        return False
def printMat(a):
    for i in range(3):
        for j in range(3):
            if a[i][j] == 'B':
                print(end="  ")
            else:
                print(a[i][j], end=" ")
        print()

def checkValid(curstate,row,col):
    if row>2 or row<0:
        return False
    else:
        if col > 2 or col < 0:
            return False
        else:
            if curstate[row][col] == 'B':
                return True
            else:
                return False

def mainOps(start):
    curstate = start
    i = 0
    turn = 0
    while len(curstate)!=9:
        if checkWin(curstate):
            print("GAME FINISHED")
            printMat(curstate)
            break
        if checkFull(curstate):
            print("MATCH IS DRAW")
            printMat(curstate)
            break
        if i%2==0:
            turn = 0
        else:
            turn = 1
        if turn == 0:
            row, col = input("Enter the position to fill as ROW COLUMN:  ").split()
            row = int(row)
            col = int(col)
            if checkValid(curstate,row,col):
                print("HUMAN'S TURN")
                curstate[row][col] = 'X'
                i = i + 1
                printMat(curstate)
            else:
                continue
        else:
            row = randint(0, 2)
            col = randint(0, 2)
            if checkValid(curstate, row, col):
                print("MACHINE'S TURN")
                curstate[row][col] = 'O'
                i = i + 1
                printMat(curstate)
            else:
                continue

if __name__ == '__main__':
    start = list()
    start = [['B','B','B'],['B','B','B'],['B','B','B']]
    mainOps(start)

#REMOVE THIS BEFORE SUBMISSION WINNING SEQ: 11 22 02 20
from random import randint
def on_board(board, x, y):
    try:
        board[int(x)][int(y)]
    except IndexError:
        return False
    else:
        return True
def getRow(x,y):
    return x
def getCol(x,y):
    return y
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
def ProbabWinX(curstate,row,col):
    diagonal = [[(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]
    bCount = 0
    cCount = 0
    dCount = 0
    eCount = 0
    for i in range(3):
        if curstate[row][i] == 'X':
            bCount = bCount+1
        else:
            continue
    for j in range(3):
        if curstate[j][col] == 'X':
            cCount = cCount+1
    if (row,col) in diagonal[0]:
        for j in diagonal[0]:
            if (row,col) == j:
                continue
            else:
                x = j
                temprow = getRow(*x)
                tempcol = getCol(*x)
                if curstate[temprow][tempcol] == 'X':
                    dCount = dCount+1
    if (row,col) in diagonal[1]:
        for j in diagonal[1]:
            if (row,col) == j:
                continue
            else:
                y = j
                temprow = getRow(*y)
                tempcol = getCol(*y)
                if curstate[temprow][tempcol] == 'X':
                    eCount = eCount + 1
    if bCount == 2 or cCount == 2 or dCount == 2 or eCount == 2:
        return True
    else:
        return False
def ProbabWin(curstate,row,col):
    diagonal = [[(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]
    bCount = 0
    cCount = 0
    dCount = 0
    eCount = 0
    for i in range(3):
        if curstate[row][i] == 'O':
            bCount = bCount+1
        else:
            continue
    for j in range(3):
        if curstate[j][col] == 'O':
            cCount = cCount+1
    if (row,col) in diagonal[0]:
        for j in diagonal[0]:
            if (row,col) == j:
                continue
            else:
                x = j
                temprow = getRow(*x)
                tempcol = getCol(*x)
                if curstate[temprow][tempcol] == 'O':
                    dCount = dCount+1
    if (row,col) in diagonal[1]:
        for j in diagonal[1]:
            if (row,col) == j:
                continue
            else:
                y = j
                temprow = getRow(*y)
                tempcol = getCol(*y)
                if curstate[temprow][tempcol] == 'O':
                    eCount = eCount + 1
    if bCount == 2 or cCount == 2 or dCount == 2 or eCount == 2:
        return True
    else:
        return False
def HeurVal(curstate,row,col):
    diagonal = [[(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)]]
    bCount = 0
    cCount = 0
    dCount = 0
    eCount = 0
    heurVal = 0
    for i in range(3):
        if curstate[row][i] == 'B':
            bCount = bCount+1
        else:
            continue
    for j in range(3):
        if curstate[j][col] == 'B':
            cCount = cCount+1
    if (row,col) in diagonal[0]:
        for j in diagonal[0]:
            if (row,col) == j:
                continue
            else:
                x = j
                temprow = getRow(*x)
                tempcol = getCol(*x)
                if curstate[temprow][tempcol] == 'B':
                    dCount = dCount+1
    if (row,col) in diagonal[1]:
        for j in diagonal[1]:
            if (row,col) == j:
                continue
            else:
                y = j
                temprow = getRow(*y)
                tempcol = getCol(*y)
                if curstate[temprow][tempcol] == 'B':
                    eCount = eCount + 1
    if bCount ==3:
        heurVal = heurVal+1
    if cCount ==3:
        heurVal = heurVal+1
    if dCount ==2:
        heurVal = heurVal+1
    if eCount ==2:
        heurVal = heurVal+1
    return heurVal
def mainOps(start):
    curstate = start
    i = 0
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
            maxheur = -999
            finrow = 0
            fincol = 0
            row, col = input("Enter the position to fill as ROW COLUMN:  ").split()
            row = int(row)
            col = int(col)
            if checkValid(curstate,row,col):
                print("HUMAN'S TURN")
                curstate[row][col] = 'X'
                i = i + 1
                printMat(curstate)
            else:
                print("INVALID MOVE!!! TRY AGAIN")
                continue
        else:
            for x in range(3):
                row = x
                win = False
                for j in range(3):
                    col = j
                    curheur = 0
                    canWin = False
                    xWin = False
                    if curstate[x][j] == 'B':
                        canWin = ProbabWin(curstate,row,col)
                        xWin = ProbabWinX(curstate,row,col)
                        if canWin:
                            print("I CAN WIN NOW")
                            finrow = row
                            fincol = col
                            win = True
                            break
                        elif xWin:
                            print("DANGER X CAN WIN NOW!!!")
                            finrow = row
                            fincol = col
                            win = True
                            break
                        else:
                            curheur = HeurVal(curstate, row, col)
                            if curheur > maxheur:
                                maxheur = curheur
                                finrow = row
                                fincol = col

                if win:
                    break
            if checkValid(curstate, finrow, fincol):
                print("MACHINE'S TURN")
                curstate[finrow][fincol] = 'O'
                i = i + 1
                printMat(curstate)
            else:
                continue

if __name__ == '__main__':
    start = list()
    start = [['B','B','B'],['B','B','B'],['B','B','B']]
    mainOps(start)

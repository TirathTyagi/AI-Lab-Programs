import sys
import time
def printMat(a):
    for i in range(3):
        for j in range(3):
            print(a[i][j],end=" ")
        print()
def checkValid(curb,operation):
    if operation == 'UP':
        if (curb[0][0] - 1) <0 or (curb[0][0] - 1) >= 3:
            return False
        else:
            return True
    if operation == 'DOWN':
        if (curb[0][0] + 1) < 0 or (curb[0][0] + 1) >= 3:
            return False
        else:
            return True
    if operation == 'LEFT':
        if (curb[0][1] - 1) < 0 or (curb[0][1] - 1) >= 3:
            return False
        else:
            return True
    if operation == 'RIGHT':
        if (curb[0][1] + 1) < 0 or (curb[0][1] + 1) >= 3:
            return False
        else:
            return True
def swap(mat,a,b,c,d):
    temp = mat[a][b]
    mat[a][b] = mat[c][d]
    mat[c][d] = temp;
def operations(a,curb,goalb):
    while True:
        if a == goalb:
            print("CONGRATS GAME COMPLETE")
            break
        operation = input("Enter Operation: UP/DOWN/LEFT/RIGHT/CURRENT/EXIT: ")
        if operation == 'CURRENT':
            printMat(a)
        if operation == 'EXIT':
            print("DO YOU WANT TO GIVE UP? YES/NO")
            inp = input()
            if inp == 'YES':
                print("QUITTING GAME...")
                time.sleep(3)
                break
            elif inp == 'NO':
                continue
        if operation == 'UP':
            if checkValid(curb,operation):
                swap(a, curb[0][0], curb[0][1], curb[0][0] - 1, curb[0][1])
                curb[0][0] = curb[0][0] - 1
                printMat(a)
            else:
                print("INVALID MOVE!!!")
                printMat(a)
        if operation == 'DOWN':
            if checkValid(curb, operation):
                swap(a, curb[0][0], curb[0][1], curb[0][0] + 1, curb[0][1])
                curb[0][0] = curb[0][0] + 1
                printMat(a)
            else:
                print("INVALID MOVE!!!")
                printMat(a)
        if operation == 'LEFT':
            if checkValid(curb, operation):
                swap(a, curb[0][0], curb[0][1], curb[0][0], curb[0][1] - 1)
                curb[0][1] = curb[0][1] - 1
                printMat(a)
            else:
                print("INVALID MOVE!!!")
                printMat(a)
        if operation == 'RIGHT':
            if checkValid(curb, operation):
                swap(a, curb[0][0], curb[0][1], curb[0][0], curb[0][1] + 1)
                curb[0][1] = curb[0][1] + 1
                printMat(a)
            else:
                print("INVALID MOVE!!!")
                printMat(a)
if __name__ == '__main__':
    start = list()
    goal = list()
    curb = []
    gob = []
    print("INPUT THE MATRIX: Press B for blank space")
    print("INPUT THE STARTING MATRIX")
    for i in range(3):
        s = []
        print("ROW:",i+1)
        for h in range(3):
            inp = input("Enter num: ")
            if inp == 'B':
                s.append(inp)
                curb.append([i,h])
            else:
                inp = int(inp)
                s.append(inp)
        start.append(s)
    print("INPUT THE GOAL MATRIX")
    for i in range(3):
        s = []
        print("ROW:",i+1)
        for j in range(3):
            inp = input("Enter Num: ")
            if inp == 'B':
                s.append(inp)
                gob.append([i,j])
            else:
                inp = int(inp)
                s.append(inp)
        goal.append(s)
    print("GOAL MATRIX: ")
    printMat(goal)
    print("STARTING MATRIX: ")
    printMat(start)
    print("STARTING GAME...")
    time.sleep(3)
    operations(start,curb,goal)

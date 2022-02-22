from collections import deque
from copy import deepcopy


def swap(mat, a, b, c, d):
    temp = mat[a][b]
    mat[a][b] = mat[c][d]
    mat[c][d] = temp


def ops(a, curb, operation):
    if operation == 'UP':
        if checkValid(curb, operation):
            swap(a, curb[0][0], curb[0][1], curb[0][0] - 1, curb[0][1])
            curb[0][0] = curb[0][0] - 1
            return a
        else:
            return -1
    if operation == 'DOWN':
        if checkValid(curb, operation):
            swap(a, curb[0][0], curb[0][1], curb[0][0] + 1, curb[0][1])
            curb[0][0] = curb[0][0] + 1
            return a
        else:
            return -1
    if operation == 'LEFT':
        if checkValid(curb, operation):
            swap(a, curb[0][0], curb[0][1], curb[0][0], curb[0][1] - 1)
            curb[0][1] = curb[0][1] - 1
            return a
        else:
            return -1
    if operation == 'RIGHT':
        if checkValid(curb, operation):
            swap(a, curb[0][0], curb[0][1], curb[0][0], curb[0][1] + 1)
            curb[0][1] = curb[0][1] + 1
            return a
        else:
            return -1


def printMat(a):
    for i in range(3):
        for j in range(3):
            if a[i][j] == 'B':
                print(end="  ")
            else:
                print(a[i][j], end=" ")
        print()


def checkValid(curb, operation):
    if operation == 'UP':
        if (curb[0][0] - 1) < 0 or (curb[0][0] - 1) >= 3:
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


def operations(a, curb, goalb):
    states = deque()
    states.append(a)
    curbs = deque()
    curbs.append(curb)
    parents = dict()
    disty = dict()
    operation = ['UP', 'DOWN', 'RIGHT', 'LEFT']
    path = []
    let = 'A'
    while len(states) > 0:
        addlist = list()
        currstat = states.popleft()
        currcurb = curbs.popleft()
        if currstat == goalb:
            print("FOUND")
            newstate  = goalb
            ez = len(path)
            printMat(goal)
            while newstate != start:
                for i,j in parents.items():
                    if j.__contains__(newstate):
                        newstate = disty[i]
                        break
                print("↑")
                print("|")
                print("|")
                printMat(newstate)
            break
        if currstat in path:
            continue
        path.append(currstat)
        for i in operation:
            original = deepcopy(currstat)
            tempcurb = deepcopy(currcurb)
            temp = ops(original, tempcurb, i)
            if temp == -1:
                continue
            states.append(temp)
            curbs.append(tempcurb)
            addlist.append(temp)
        disty[let] = currstat
        parents[let] = addlist
        let = chr(ord(let)+1)

if __name__ == '__main__':
    start = list()
    goal = list()
    curb = list()
    gob = list()
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
    print("COMPUTING RESULT...")
    operations(start, curb, goal)

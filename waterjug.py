from collections import deque


def waterjug(a, b, goal):
    states = deque()
    path = []
    visit = {}
    states.append((0, 0))
    while len(states) > 0:
        pre = states.popleft()
        if pre[0] > a or pre[1] > b or pre[0] < 0 or pre[1] < 0:
            continue
        if (pre[0], pre[1]) in visit:
            continue
        path.append([pre[0], pre[1]])
        visit[(pre[0], pre[1])] = 1
        if pre[0] == goal or pre[1] == goal:
            if pre[0] == goal and pre[1] != 0:
                path.append([pre[0], 0])
            elif pre[1] == goal and pre[0] != 0:
                path.append([0, pre[1]])
                path.append([pre[1], 0])
            ez = len(path)
            print("FORMAT: (Jug 1,Jug 2)")
            for i in range(ez):
                print("(", path[i][0], ",", path[i][1], ")")
            break
        if a > b:
            states.append((pre[0], b))
        else:
             states.append((a, pre[1]))
        for i in range(max(a, b) + 1):
            add = pre[0] + i
            sub = pre[1] - i
            if add == a or (sub==0 and sub>=0):
                states.append((add,sub))
            add = pre[1] + i
            sub = pre[0] - i
            if add == b or (sub==0 and sub>=0):
                states.append((sub,add))
        if a > b:
            states.append((0, b))
        else:
            states.append((a, 0))


if __name__ == '__main__':
    a = int(input("Enter capacity of JUG 1: "))
    b = int(input("Enter capacity of JUG 2: "))
    c = int(input("Enter target volume for JUG 1: "))
    waterjug(a, b, c)

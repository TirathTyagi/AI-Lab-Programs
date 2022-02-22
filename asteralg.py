import sys
from collections import deque
def distfromstart(graph,heur,start,f,q,visit):
    for i in graph[start]:
        temp = f[start] + graph[start][i] + heur[i]
        if i in visit:
            if f[i] > temp:
                f[i] = temp
            continue
        if i not in f:
            f[i] = temp
        q.append(i)
        visit.append(i)
        continue
    start = q.popleft()
    while len(q) > 0:
        distfromstart(graph, heur, start, f, q,visit)
    return f


def astarall(graph,heur,start,goal):
    tempq = deque()
    visitq = []
    f = dict()
    f[start] = 0
    f = distfromstart(graph,heur,start,f,tempq,visitq)
    path = []
    q = deque()
    q.append(goal)
    while len(q) > 0:
        cur = q.popleft()
        path.append(cur)
        if cur is start:
            break
        mindist = sys.maxsize
        for i in graph[cur]:
            if f[i] < mindist:
                mindist = f[i]
                cur = i
        q.append(cur)
        continue
    path.reverse()
    leny = len(path)
    for i in range(leny):
        if i is leny-1:
            print(path[i])
            break
        print(path[i],end="->")

if __name__ == '__main__':
    graph = dict()
    heur = dict()
    while True:
        c = input("INPUT FORMAT: NODE NODE DIST\n")
        if c == 'done':
            break
        node1, node2, weight = c.split()
        weight = int(weight)
        if node1 not in graph:
            graph[node1] = {}
        if node2 not in graph:
            graph[node2] = {}
        graph[node1][node2] = weight
        graph[node2][node1] = weight

    for i in graph:
        print("Input heuristic value for edge",i,": ")
        h = int(input())
        heur[i] = h

    goal = input("Enter destination node: ")
    start = input("Enter starting node: ")
    astarall(graph,heur,start,goal)

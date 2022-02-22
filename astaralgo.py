import sys
from collections import deque
def astarall(graph,heur,start,goal):
    visited = []
    q = deque()
    for i in graph:
        q.append(i)
    cur = start
    while len(q) > 0:
        minnum = sys.maxsize
        minkey = sys.maxsize
        print(q)
        q.remove(cur)
        print(cur)
        visited.append(cur)
        if cur is goal:
            print(visited)
            break
        for i in graph[cur]:
            if i in visited:
                continue
            temp = heur[i] + graph[cur][i]
            if temp < minnum :
                minkey = i
                minnum = temp
        print(minnum)
        cur = minkey
        continue


if __name__ == '__main__':
    graph = dict()
    heur = dict()
    while True:
        c = input("INPUT FORMAT: NODE NODE : DIST\n")
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
    print(graph)
    print(heur)
    astarall(graph,heur,start,goal)

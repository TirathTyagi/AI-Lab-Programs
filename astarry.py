import sys
def astarsolve(graph, heur, start, goal):
    print(graph)
    print(heur)
    open_list = []
    close_list = []
    g = {}
    parents = {}
    parents[start] = start
    g[start] = 0
    open_list.append(start)
    while len(open_list) > 0:
        curr = None
        minF = sys.maxsize
        for i in open_list:
            if (g[i] + heur[i]) < minF:
                curr = i
                minF = g[i] + heur[i]
        open_list.remove(curr)
        if curr is goal:
            close_list.append(curr)
            reconst_path = []
            while parents[curr] != curr:
                reconst_path.append(curr)
                curr = parents[curr]
            reconst_path.append(start)
            reconst_path.reverse()
            num = len(reconst_path)
            for i in range(num):
                if i is num - 1:
                    print(reconst_path[i])
                    break
                print(reconst_path[i], end='->')
            print("COST:", g[reconst_path[num - 1]])
        for i in graph[curr]:
            if i not in open_list and i not in close_list:
                open_list.append(i)
                parents[i] = curr
                g[i] = g[curr] + graph[curr][i]
            else:
                if g[i] > g[curr] + graph[curr][i]:
                    g[i] = g[curr] + graph[curr][i]
                    parents[i] = curr
                    if i in close_list:
                        close_list.remove(i)
                        open_list.append(i)
        close_list.append(curr)
        if graph[curr] is None:
            print("CANNOT BE SOLVED")


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
        print("Input heuristic value for edge", i, ": ")
        h = int(input())
        heur[i] = h
    goal = input("Enter destination node: ")
    start = input("Enter starting node: ")
    astarsolve(graph, heur, start, goal)

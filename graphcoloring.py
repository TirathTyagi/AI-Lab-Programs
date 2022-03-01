from collections import deque
def checkAdjacency(graph,graphcolor,color,i):
    for j in graph[i]:
        if graphcolor[j] == color:
            return False
        else:
            continue
    return True
def getChromaticNumber(graphcolor):
    colorused = []
    for i in graphcolor:
        if graphcolor[i] in colorused:
            continue
        else:
            colorused.append(graphcolor[i])
    return len(colorused)
def mainOps(graph):
    graphcolor = dict()
    for i in graph:
        graphcolor[i] = 'N'
    for i in graph:
        color = ['Red', 'Blue', 'Green', 'Yellow',  'Black','Pink','Orange','White','Gray','Purpul','Brown','Navy']
        for j in color:
            if checkAdjacency(graph,graphcolor,j,i):
                graphcolor[i] = j
                break
            else:
                continue
    for i in graphcolor:
        print("NODE:",i,end="||")
        print("Color:",graphcolor[i])
    print("CHROMATIC NUMBER:",getChromaticNumber(graphcolor))
if __name__ == '__main__':
    graph = dict()
    while True:
        c = input("INPUT FORMAT: NODE NODE DIST\n")
        if c == 'done':
            break
        node1, node2 = c.split()
        if node1 not in graph:
            graph[node1] = {}
        if node2 not in graph:
            graph[node2] = {}
        graph[node1][node2] = 0
        graph[node2][node1] = 0
    print("----------------------RESULT-------------------------")
    mainOps(graph)
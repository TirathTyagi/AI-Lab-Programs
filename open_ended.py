from collections import defaultdict,deque
from itertools import combinations
def min_cover(graph,n,m,tbv):
    print("lol")
    for i in range(len(tbv)):
        for j in combinations(tbv,i):
            print(j)
if __name__ == '__main__':
    m = int(input("Enter the total representatives of country A: "))
    n = int(input("Enter the total representatives of country B: "))
    k = int(input("Enter the total pairs chosen for delegation: "))
    i = 0
    l1 = list()
    visited= defaultdict(list)
    total_elems = deque()
    while i<k:
        p = input("Enter pairs: ").split()
        p[0] = int(p[0])
        p[1] = int(p[1])
        if p[0] > m or p[1] > n:
            print("INVALID PAIRS!!!!")
            exit(1)
        p[1] = chr(ord('@') + int(p[1]))
        if p[0] not in total_elems:
            total_elems.append(p[0])
        if p[1] not in total_elems:
            total_elems.append(p[1])
        visited[p[0]].append(p[1])
        visited[p[1]].append(p[0])
        l1.append(p)
        i = i+1
    print(visited)
    print(total_elems)
    min_cover(visited,n,m,total_elems)

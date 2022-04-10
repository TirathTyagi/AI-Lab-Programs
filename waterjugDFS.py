import sys


class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("EMPTY FRONTIER")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class WaterJug():
    def __init__(self, start, cap1, cap2, goal):
        self.start = start
        self.cap1 = cap1
        self.cap2 = cap2
        self.goal = goal

    def neighbors(self, state):
        j1, j2 = state
        candidates = []
        if j1 + j2 <= self.cap1:
            candidates.append(("Fill 1 using 2", (j1 + j2, 0)))
        if j1 + j2 <= self.cap2:
            candidates.append(("Fill 2 using 1", (0, j1 + j2)))
        if j1 > 0:
            candidates.append(("Empty 1", (0, j2)))
        if j2 > 0:
            candidates.append(("Empty 2", (j1, 0)))
        if j1 < self.cap1:
            candidates.append(("Fill 1", (self.cap1, j2)))
        if j2 < self.cap2:
            candidates.append(("Fill 2", (j1, self.cap2)))
        if j1 + j2 >= self.cap1 and j2 > 0:
            candidates.append(("Empty 2 to 1", (self.cap1, j2 - (self.cap1 - j1))))
        if j1 + j2 >= self.cap2 and j1 > 0:
            candidates.append(("Empty 1 to 2", (j1 - (self.cap2 - j2), self.cap2)))
        return candidates

    def Solve(self):
        self.numexp = 0
        start = Node(state=self.start, parent=None, action=None)
        frontier = StackFrontier()
        frontier.add(start)
        self.explored = set()
        while True:
            if frontier.empty():
                raise Exception("There is no solution")
            node = frontier.remove()
            print(node.state)
            self.numexp += 1
            if node.state == self.goal:
                action = []
                cells = []
                while node.parent is not None:
                    action.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                action.reverse()
                cells.reverse()
                self.solution = (action, cells)
                return
            self.explored.add(node.state)
            for i, j in self.neighbors(node.state):
                if not frontier.contains_state(j) and j not in self.explored:
                    child = Node(j, node, i)
                    frontier.add(child)


if __name__ == '__main__':
    start = (0, 0)
    cap1 = int(input("Enter capacity of jug 1: "))
    cap2 = int(input("Enter capacity of jug 2: "))
    goaly = int(input("Enter the goal capacity: "))
    if goaly > cap1 or goaly > cap2:
        raise Exception("INVALID GOAL!!!!")
    buck = input("Enter the jug to reach goal (1 OR 2) : ")
    buck  = int(buck)
    if buck == 1:
        goal = (goaly, 0)
    elif buck == 2:
        goal = (0, goaly)
    else:
        raise Exception("INVALID JUG!!!!")
    waterjug = WaterJug(start, cap1, cap2, goal)
    waterjug.Solve()

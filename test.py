def getRow(x,y):
    return x
def getCol(x,y):
    return y
diagonal = [[(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)]]
for i in diagonal:
    for j in i:
        x = j
        print(getRow(*x))

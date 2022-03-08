from itertools import combinations
def bruteForce(items,weightlim):
    print()
    print("------------------RESULT---------------------")
    itemList = list()
    remList = list()
    maxCost = 0
    maxWeight = 0
    maxList = list()
    for i,j in items.items():
        itemList.append(i)
    for n in range(len(itemList)):
        remList+=list(combinations(itemList,n))
    remList.append((1,2,3,4))
    remList.remove(())
    for i in remList:
        curCost = 0
        curWeight = 0
        curList = list()
        for j in i:
            curList.append(j)
        for h in curList:
            curCost = curCost + items[h][0]
            curWeight = curWeight + items[h][1]
        if len(curList) == 1:
            print(curList, end="    || ")
        else:
            print(curList, end=" || ")
        print("TOTAL COST: ", curCost, end=" || ")
        if curWeight > weightlim:
            curWeight = 'Not Feasible'
        print("TOTAL WEIGHT: ", curWeight)
        if curWeight != 'Not Feasible':
            if curCost>maxCost:
                maxCost = curCost
                maxList = curList
                maxWeight = curWeight
        print()
    print()
    print("SUBSET: ",maxList)
    print("MAX COST: ",maxCost)
    print("WEIGHT: ",maxWeight)
    print("------------------RESULT---------------------")
if __name__ == '__main__':
    items = dict()
    i  = 1
    while True:
        inItem = input("Enter item Cost: ")
        if inItem == 'done':
            break
        weiItem = input("Enter item Weight: ")
        inItem = int(inItem)
        weiItem = int(weiItem)
        detTup = (inItem,weiItem)
        items[i] = detTup
        i = i + 1
    weightLim = input("Enter weight Limit: ")
    weightLim = int(weightLim)
    print(items)
    bruteForce(items,weightLim)
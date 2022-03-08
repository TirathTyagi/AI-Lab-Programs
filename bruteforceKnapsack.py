def bruteForce(items,weightlim):
    print()
    print("------------------RESULT---------------------")
    for i,j in items.items():
        for k,l in items.items():
            curList = list()
            curCost = 0
            curWeight = 0
            curList.append(i)
            if i != k:
                curList.append(k)
            for h in curList:
                curCost = curCost + items[h][0]
                curWeight = curWeight + items[h][1]
            if len(curList) == 1:
                print(curList, end="    || ")
            else:
                print(curList, end=" || ")
            print("TOTAL COST: ",curCost,end=" || ")
            if curWeight > weightlim:
                curWeight = 'Not Feasible'
            print("TOTAL WEIGHT: ",curWeight)
            print()
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
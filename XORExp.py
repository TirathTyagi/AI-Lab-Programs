def ORGate(input1,input2):
    if input1+input2>0:
        return 1
    else:
        return 0
def ANDGate(input1,input2):
    if input1 == input2:
        return input1
    else:
        return 0
def NOTGate(input):
    if input == 0:
        return 1
    elif input == 1:
        return 0
    else:
        raise Exception("INVALID INPUT")
def XORGate(l1,l2):
    listy = list()
    for i in l1:
        h = NOTGate(i) # NOT OF A
        for j in l2:
            k = NOTGate(j) # NOT OF B
            l = ANDGate(i,k)
            m = ANDGate(j,h)
            listy.append(ORGate(l,m))
    return listy
if __name__ == '__main__':
    a = [0,1]
    b = [0,1]
    c = [0,1]
    listy = XORGate(a,b)
    k = 0
    l = 0
    listy2 = XORGate(c,listy)
    print("-----------------TRUTH TABLE FOR 3 INPUT XOR GATE-------------------")
    print("A            B         A ⊕ B")
    print("--------------------------")
    for i in a:
        for j in b:
            print(i, "     |    ", j, "    |    ", listy[k])
            k = k + 1
    print("--------------------------------------------------------------------")
    print("C          A ⊕ B     A ⊕ B ⊕ C")
    print("----------------------------")
    for i in c:
        for j in listy:
            print(i, "     |    ", j, "    |    ", listy2[l])
            l = l + 1
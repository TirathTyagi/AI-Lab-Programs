def dfs(x):
    for j in range(n+1):
        if (v[j]!=1) and matrix[x][j] == 1:
            v[j] = 1
            if pre[j] == 0 or dfs(pre[j]):
                pre[j] = i
                return 1
    return 0
m = int(input("Enter the total representatives of country A: "))
n = int(input("Enter the total representatives of country B: "))
k = int(input("Enter the total pairs chosen for delegation: "))
sol = m+n
matrix = []
pre = [0]*1100
for i in range(m+1):
    a = []
    for j in range(n+1):
        a.append(0)
    matrix.append(a)
i = 0
while i < k:
    s = input("Enter pairs: ").split()
    l = int(s[0])
    m = int(s[1])
    matrix[l-1][m-1] = 1
    i=i+1
ans = 0
for i in range(1,m+2):
    v = [0]*1100
    if dfs(i):
        ans= ans+1
print("Minimum number of telephone lines: ",sol-ans)

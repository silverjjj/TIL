N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
arr.sort(key=lambda x:x[0])
L = arr[-1][0]+1
weight = [0]*L
maxY, maxX = 0,0
for x,y in arr:
    weight[x] = y
    if y > maxY:
        maxY = y
        maxX = x
res = 0
for i in range(maxX):
    res += max(weight[:i+1])
for j in range(maxX, L):
    res += max(weight[j:])
print(res)

'''
8
2 4
11 4
15 8
4 6
5 3
8 10
13 6
16 8
'''
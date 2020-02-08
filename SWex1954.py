N = int(input())
arr = [[-1]*N for _ in range(N)]

print(arr)
case = [(0,1),(1,0),(0,-1),(-1,0)]
cnt = 0
arr2 = []
for i in range(N):
    for j in range(N):
        arr2.append(arr[i][j]+1)
print(arr2)
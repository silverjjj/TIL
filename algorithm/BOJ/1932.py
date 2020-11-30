N = int(input())
weight = [0]*(N)
arr = [list(map(int,input().split())) for _ in range(N)]
for i in range(1,N+1):
    for j in range(i+1):
        arr[i][j] = arr[i-1][j]
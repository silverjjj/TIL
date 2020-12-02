import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
weight = [[0] * i for i in range(1,N+1)]
weight[0][0] = arr[0][0]
for i in range(N-1):
    for j in range(i+1):
        weight[i+1][j] = max(weight[i+1][j], weight[i][j]+arr[i+1][j])
        weight[i + 1][j+1] = max(weight[i + 1][j+1], weight[i][j] + arr[i + 1][j+1])
print(max(weight[-1]))
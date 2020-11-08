import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(2)]
    weight = [[0 for _ in range(n)] for _ in range(2)]
    weight[0][0] = arr[0][0]
    weight[1][0] = arr[1][0]
    if n == 2:
        weight[0][1] = arr[1][0] + arr[0][1]
        weight[1][1] = arr[0][0] + arr[1][1]
    elif n >= 3:
        weight[0][1] = arr[1][0] + arr[0][1]
        weight[1][1] = arr[0][0] + arr[1][1]
        for j in range(2,n):
            for i in range(2):
                if i == 0:
                    weight[i][j] = max(weight[i + 1][j - 1], weight[i + 1][j - 2])
                else:
                    weight[i][j] = max(weight[i-1][j-1], weight[i-1][j-2])
                weight[i][j] += arr[i][j]
    res = max(weight[0][-1],weight[1][-1])
    print(res)
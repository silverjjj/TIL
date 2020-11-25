import sys
input = sys.stdin.readline

weight = [[0]*41 for _ in range(2)]
weight[0][0], weight[1][0] = 1,0
weight[0][1], weight[1][1] = 0,1
for j in range(2,41):
    weight[0][j] = weight[0][j-1] + weight[0][j-2]
    weight[1][j] = weight[1][j-1] + weight[1][j-2]
T = int(input())
for _ in range(T):
    num = int(input())
    print(weight[0][num], weight[1][num])
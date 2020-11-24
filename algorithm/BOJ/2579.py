'''
BOJ2579
'''
import sys
input= sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]
weight = [[0,0] for _ in range(N)]
if N >= 1:
    weight[0][0] = arr[0]
    weight[0][1] = arr[0]
if N >= 2:
    weight[1][0] = arr[0] + arr[1]
    weight[1][1] = arr[1]
    for i in range(2,N):
        weight[i][0] = arr[i] + weight[i-1][1]
        weight[i][1] = arr[i] + max(weight[i-2][0],weight[i-2][1])
print(max(weight[-1]))
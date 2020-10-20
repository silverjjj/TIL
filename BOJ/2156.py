import sys
input = sys.stdin.readline
N = int(input())
weight = [0]
for i in range(N):
    weight.append(int(input()))
dp = [0]
dp.append(weight[1])
if N >= 2:
    dp.append(weight[1] + weight[2])
for i in range(3,N+1):
    dp.append(max(dp[i-1], dp[i-2]+weight[i], dp[i-3]+weight[i-1]+weight[i]))
print(dp[N])
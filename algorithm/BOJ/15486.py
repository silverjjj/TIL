import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [0]*(N+1)
for idx in range(N):
    if 0 <= idx + arr[idx][0] <= N:
        dp[(arr[idx][0]+idx)] = max(dp[arr[idx][0]+idx], dp[idx] + arr[idx][1])
    dp[idx+1] = max(dp[idx+1],dp[idx])
print(dp[N])
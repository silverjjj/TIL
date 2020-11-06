'''
BOJ 11047
'''
import sys
input = sys.stdin.readline
N,K = map(int,input().split())
coins = [int(input()) for _ in range(N)]
coins = coins[::-1]
won = K
res = 0
for coin in coins:
    if coin > won:
        continue
    res += (won // coin)
    won = won % coin
print(res)

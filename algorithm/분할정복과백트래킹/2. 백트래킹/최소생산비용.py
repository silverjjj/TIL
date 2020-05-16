# SWex 5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용
# nqueen과 문제유형 비슷
def dfs(y,sum):
    global minV
    if sum > minV:  # 가지치기
        return
    if y == n:      # 목표달성
        if minV > sum:
            minV= sum
    for x in range(n):  # 완전탐색
        if not fectory[x]:
            fectory[x] = 1
            dfs(y+1, sum+rm[x][y])
            fectory[x] = 0

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    rm = [list(map(int,input().split())) for _ in range(n)]
    fectory =[0]*n
    minV = 12345678
    dfs(0,0)
    print("#{} {}".format(tc, minV))

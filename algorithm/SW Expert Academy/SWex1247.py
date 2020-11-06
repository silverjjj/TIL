#SWex 1247. [S/W 문제해결 응용] 3일차 - 최적 경로
def dfs(x,y,k,result):
    global minV
    if result >= minV:
        return

    if k == n:
        result += (abs(x-home[0]) + abs(y-home[1]))
        if minV > result:
            minV = result
        return

    for i in range(n):
        if not visited[i]:  # 방문표시
            visited[i] = 1
            # 실시간으로 result를 더하면서 가지치기를 위해 result값도 재귀로 돌려줘야함
            dfs(work[2*i], work[(2*i)+1], k+1, result + abs(x - work[2*i]) + abs(y - work[2*i+1]))
            visited[i] = 0


T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    minV = 1234567
    visited = [0] * n
    comp = [arr[0],arr[1]]; home = [arr[2], arr[3]]; work = arr[4:]
    dfs(comp[0],comp[1],0,0)
    print("#{} {}".format(tc,minV))
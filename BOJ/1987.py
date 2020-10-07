import sys
read = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,1,-1]
def bfs(x,y,mapping):
    q = set([])
    q.add((x,y,mapping[x][y]))
    maxV = 1
    while q:
        # print(q)
        x,y,ans = q.pop()       # set 데이터타입에서 pop()함수는 임의의원소를 반환한다
        # print(x,y,ans)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<m and mapping[nx][ny] not in ans:
                q.add((nx,ny,ans + mapping[nx][ny]))
                maxV = max(maxV, len(ans)+1)
    return maxV
n, m = map(int,input().split())
mapping = [list(read().strip()) for _ in range(n)]
print(bfs(0,0,mapping))

'''
c

2 4
CAAB
ADCB
'''
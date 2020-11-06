# SWex1949. [모의 SW 역량테스트] 등산로 조성
'''
1. 가장 큰숫자의 좌표를 찾는다.
2. 해당 좌표를 출발점으로 하여 상하좌우를 이동한다.
3. 이동할때는 조건이 존재한다=>방문x and 현재위치보다 작은숫자,
만약에 상하좌우 전부 현재숫자보다 크거나 같다면 k범위안으로 -1씩하면서 가능성을 찾아보자
4. 만약에 한차례 -를 진행 했다면, flag를 통해 표시를 해준다
5. 이동한다면 재귀를 통한 다음 함수로 이동
6 만약 3~4번의 조건에서도 이동할 방향이 없다면, 이 전의 함수로 return
'''
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x,y,height,flag):
    global maxV
    visited[x][y] = 1
    if height > maxV:
        maxV = height
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
            if mapping[x][y] > mapping[nx][ny]:
                bfs(nx,ny,height+1,flag)
            elif flag:
                for i in range(1, K+1):
                    mapping[nx][ny] -= i
                    if mapping[x][y] > mapping[nx][ny]:
                        bfs(nx, ny, height + 1, False)
                    mapping[nx][ny] += i
    visited[x][y] = 0

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    mapping = [list(map(int,input().split())) for _ in range(N)]
    high = 0
    maxV = 0
    for row in mapping:
        if max(row) > high:
            high=max(row)
    result = 0
    for i in range(N):
        for j in range(N):
            if mapping[i][j] == high:
                visited = [[0]*N for _ in range(N)]
                bfs(i,j,1,True)
                if maxV > result:
                    result = maxV
    print("#{} {}".format(tc,result))
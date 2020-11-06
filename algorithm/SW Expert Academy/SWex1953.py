# bfs
def find(sx,sy):
    # print("---------")
    if rm[sx][sy] == 1:
        dx = [-1, 1, 0, 0]  # 상하좌우
        dy = [0, 0, -1, 1]
        mapping = [[1,2,5,6],[1,2,4,7],[1,3,4,5],[1,3,6,7]]      # 상하좌우
    elif rm[sx][sy] == 2:
        dx = [-1, 1, 0, 0]  # 상하
        dy = [0, 0, 0, 0]
        mapping = [[1,2,5,6],[1,2,4,7],[],[]]
    elif rm[sx][sy] == 3:
        dx = [0,0, 0, 0]  # 좌우
        dy = [0, 0, -1, 1]
        mapping = [[], [], [1,3,4,5], [1,3,6,7]]
    elif rm[sx][sy] == 4:
        dx = [-1, 0, 0, 0]  # 상우
        dy = [0, 0, 0, 1]
        mapping = [[1,2,5,6], [], [], [1,3,6,7]]
    elif rm[sx][sy] == 5:
        dx = [0, 1, 0, 0]  # 하우
        dy = [0, 0, 0, 1]
        mapping = [[], [1,2,4,7], [], [1,3,6,7]]
    elif rm[sx][sy] == 6:
        dx = [0, 1, 0, 0]  # 하좌
        dy = [0, 0, -1,0]
        mapping = [[], [1,2,4,7], [1,3,4,5], []]
    elif rm[sx][sy] == 7:
        dx = [-1, 0, 0, 0]  # 상좌
        dy = [0, 0, -1, 0]
        mapping = [[1,2,5,6], [], [1,3,4,5], []]
    return dx,dy,mapping
def bfs(x,y):
    cnt = 0
    visit = [[0]*m for _ in range(n)]
    # print(visit)
    q = []
    q.append((x,y))
    visit[x][y] = 1
    while q:
        sx,sy = q.pop(0)
        tmp = visit[sx][sy]
        dx, dy, mapping= find(sx,sy)
        for k in range(4):
            nx = sx + dx[k]
            ny = sy + dy[k]
            if 0<=nx<n and 0<=ny<m and visit[nx][ny] == 0 and rm[nx][ny] != 0:
                if rm[nx][ny] in mapping[k]:
                    visit[nx][ny] = tmp+1
                    q.append((nx,ny))
    for i in range(n):
        for j in range(m):
            if visit[i][j] <= l and visit[i][j] != 0:
                cnt +=1
    return cnt
T = int(input())
for tc in range(1,T+1):
    n,m,r,c,l = map(int,input().split())
    rm = [list(map(int,input().split())) for _ in range(n)]
    print("#{} {}".format(tc,(bfs(r,c))))

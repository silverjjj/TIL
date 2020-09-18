# 14503_로봇청소기
# 0:북, 1:동, 2:남, 3:서
# 해당 방향을 기준으로 왼쪽 -> 아래 -> 오른 -> 위
direction = {0:[(0,-1,3),(1,0,2),(0,1,1),(-1,0,0)],
             1:[(-1,0,0),(0,-1,3),(1,0,2),(0,1,1)],
             2:[(0,1,1),(-1,0,0),(0,-1,3),(1,0,2)],
             3:[(1,0,2),(0,1,1),(-1,0,0),(0,-1,3)]}

def DFS(mapping,visited,x,y,d):
    s = []
    s.append([x,y,d])
    visited[x][y] = 1
    cnt = 1
    while s:
        x, y, d = s.pop()
        flag = False
        for dx, dy, direct in direction[d]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and not mapping[nx][ny]:
                visited[nx][ny] = 1 # 청소 표시
                cnt += 1
                s.append([nx,ny,direct])
                flag = True
                break
        # 4방향 모두 존재 안할때
        if not flag:
            if d == 0:
                x += 1
            elif d == 1:
                y -= 1
            elif d == 2:
                x -= 1
            elif d == 3:
                y += 1
            if 0 <= x < N and 0 <= y < M and not mapping[x][y]:
                s.append([x,y,d])
            else:
                return cnt

N,M = map(int,input().split())
r,c,d = map(int,input().split())
mapping = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
print(DFS(mapping,visited,r,c,d))
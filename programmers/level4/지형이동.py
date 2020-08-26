dx = [-1,1,0,0]
dy = [0,0,1,-1]

def BFS(x,y,n,land,height):
    q = []
    tmp = []
    tmp.append([x,y])
    visited = [[0]*n for _ in range(n)]
    var = 0
    for x,y in tmp:
        if visited[x][y] != 0:
            continue
        tmp = []
        var += 1
        visited[x][y] = var
        q.append([x,y])
        while q:
            x,y = q.pop(0)
            for k in range(4):
                nx = x + dx[k]; ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                    cur_next_diff = abs(land[nx][ny] - land[x][y])  # 현재위치와 다음위치의 차이
                    if cur_next_diff <= height:
                        visited[nx][ny] = var
                        q.append([nx,ny])
                    else:
                        tmp.append([nx,ny])

    distance = [[] for _ in range(var+1)]
    for i in range(n):
        for j in range(n):
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if visited[i][j] == num and not used[i][j]:
                    s.append([i,j])
                    used[i][j] = 0
                    while s:
                        x, y = s.pop(0)
                        cur = visited[x][y]
                        for k in range(4):
                            nx = x + dx[k]; ny = y + dy[k]
                            if 0 <= nx < n and 0 <= ny < n and not used[nx][ny]:
                                next = visited[nx][ny]
                                if next != cur:     # 값이 다를경우
                                    if distance[next] == 0:
                                        distance[next] = abs(land[x][y] - land[nx][ny])
                                    elif distance[next] > abs(land[x][y] - land[nx][ny]):
                                        distance[next] = abs(land[x][y] - land[nx][ny])
                                else:           # 값이 같을경우
                                    s.append([nx, ny])
                                    used[nx][ny] = 1
    return sum(distance)
def solution(land, height):
    n = len(land[0])
    answer = BFS(0,0,n,land,height)
    return answer


land = [[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]]
height = 1
print(solution(land, height))
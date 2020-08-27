import heapq
dx = [-1,1,0,0]
dy = [0,0,1,-1]
def BFS(x,y,n,land,height):
    q = []
    visited = [[0]*n for _ in range(n)]
    var = 0
    tmp = []
    tmp.append([x,y])
    while tmp:
        i,j = tmp.pop(0)
        if visited[i][j] != 0:
            continue
        var += 1
        visited[i][j] = var
        q.append([i,j])
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
    # for row in visited:
    #     print(row)
    return visited, var

def mst_make(visited, land, n, var):
    adj = { i : [] for i in range(1,var+1)}
    for i in range(n):
        for j in range(n):
            cur = visited[i][j]
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    next = visited[nx][ny]
                    if cur < next:
                        adj[cur].append([abs(land[nx][ny] - land[i][j]),next])
                        adj[next].append([abs(land[nx][ny] - land[i][j]), cur])
    return adj
def MST(adj,var):
    # print(adj)
    INF = float('inf')
    weight = [INF]*(var+1)
    mst = [False] *(var+1)
    pq = []
    weight[1] = 0
    heapq.heappush(pq,(0,1))    # 가중치, 위치
    res = 0
    while pq:
        w, node = heapq.heappop(pq)
        if mst[node]:
            continue
        mst[node] = True
        res += w
        for w, next_node in adj[node]:
            if not mst[next_node] and weight[next_node] > w:
                weight[next_node] = w
                heapq.heappush(pq, (weight[next_node], next_node))
    return res

def solution(land, height):
    n = len(land[0])
    visited, var = BFS(0,0,n,land,height)
    adj = mst_make(visited, land, n ,var)
    res = MST(adj,var)
    return res
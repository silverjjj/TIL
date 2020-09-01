'''
상 <-> 하 or 좌 <-> 우 : 직선도로
직선도로가 직각으로 만나는지점이 코너
직선도로 => 100원
코너 ==> 500원

bfs
이전의 위치를 함수 인자에 넣자
예를들면 상하좌우 1,2,3,4로 해서 다음 위치가 3인데 이전의 위치가 1 or 2이면 500원 추가
'''
dx = [0,-1,1,0,0] # 상하좌우
dy = [0,0,0,-1,1]
minV = float('inf')
def coner(coner,pre_k,k,nx,ny,x,y):
    # 코너일경우
    add = coner[x][y]
    if ((pre_k == 1 or pre_k == 2) and (k == 3 or k == 4)) or ((pre_k == 3 or pre_k == 4) and (k == 1 or k == 2)):
        if coner[nx][ny] >= coner[x][y] + 600:
            add += 500
    # 코너가 아닐경우
    add += 100
    return add
def BFS(board, visited ,n, x, y,res):
    global minV
    q = [[x,y,0]]
    INF = float('inf')
    coner_list = [[INF] * n for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    visited[0][0] = 1
    coner_list[0][0] = 0
    while q:
        x,y,pre_k = q.pop(0)
        if x == n-1 and y == n-1:
            if minV > coner_list[n-1][n-1]:
                minV = coner_list[n-1][n-1]
            continue
        for k in range(1,5):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<n and not board[nx][ny]:
                add = coner(coner_list,pre_k,k,nx,ny,x,y)
                if not visited[nx][ny] or (coner_list[nx][ny] >= add):
                    coner_list[nx][ny] = add
                    visited[nx][ny] = 1
                    q.append([nx,ny,k])
    return minV

def solution(board):
    n = len(board)
    visited = [[0]*n for _ in range(n)]
    visited[0][0] = 1
    answer = BFS(board, visited, n, 0,0,0)
    return answer


board =[[0,0,0],[0,0,0],[0,0,0]]
# board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
solution(board)
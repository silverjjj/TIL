dx = [0,0,-1,1] # 상하좌우
dy = [1,-1,0,0]

def DFS(x,y,dirs):
    k = 0
    visited = set()
    for dir in dirs:
        if dir == 'U': k = 0
        elif dir == 'D': k = 1
        elif dir == 'L': k = 2
        elif dir == 'R': k = 3
        nx = x + dx[k]
        ny = y + dy[k]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add((x,y,nx,ny))
            visited.add((nx, ny, x, y))
            x = nx
            y = ny
    return len(visited) // 2

def solution(dirs):
    answer = DFS(0,0,dirs)

    return answer

dirs = "LULLLLLLU"
solution(dirs)
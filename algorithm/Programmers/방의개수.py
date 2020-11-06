'''
이동할때마다 모든 위치를 기록함
'''
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

def solution(arrows):
    dict = {}
    ans = x = y = 0
    q = []
    for num in arrows:
        nx = x + dx[num]
        ny = y + dy[num]
        dict[(x,y,nx,ny)] = 0   # 방향 등록
        dict[(nx,ny,x,y)] = 0
        q.append((x,y,nx,ny))       # 현재 위치 등록
        x = nx
        y = ny
    arr = [(0,0)]
    print(q)
    while q:
        sx, sy, nx,ny = q.pop(0)
        if (nx,ny) in arr:
            if dict[(sx, sy, nx,ny )] == 0:
                dict[(sx, sy, nx, ny)] = 1
                dict[(nx, ny, sx, sy)] = 1
                ans += 1
        else:
            dict[(sx, sy, nx, ny)] = 1
            dict[(nx, ny, sx, sy)] = 1
            arr.append((nx, ny))
    print(ans)
    return ans
arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]
solution(arrows)
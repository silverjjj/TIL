# SWex4875 미로

def f(x,y,N):
    global maze
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    s = []
    nx = x
    ny = y
    s.append([nx,ny])
    maze[nx][ny] = 1
    while s: # 스택에 좌표가 남아있으면
        x,y = s.pop()
        # print(x,y)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if maze[nx][ny] == 0:
                    s.append([nx,ny])
                    maze[nx][ny] = 1
                elif maze[nx][ny] == 3:
                    return 1

    return 0 # while을 빠져나온다 -> 경로를 다 돌았는데 3을 찾지 못했다.

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maze = [[int(x) for x in input()] for _ in range(N)]
    print(maze)
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                print("#{} {}".format(tc,f(i,j,N)))

















#
# def find():
#     dr = [0,1,0,-1]
#     dc = [1,0,-1,0]
#     s = []
#     s.append([sr,sc])       # start 지점을 스택에 쌓는다.
#     arr[sr][sc] = 1         # 다시 되돌아오지 못하게 1로 막아놓는다.
#     while len(s) != 0:
#         n = s.pop()
#         for i in range(4):      # 4방탐색을 통해 0을 찾는다.
#             nr = n[0] + dr[i]       # nr은 new row
#             nc = n[1] + dc[i]
#             if 0<= nr < N and 0<=nc<N:
#                 if arr[nr][nc] == 2:
#                     return 1
#                 elif arr[nr][nc] == 0:
#                     s.append([nr,nc])
#                     arr[nr][nc] = 1
#     return 0
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     arr = []
#     for i in range(N):
#         a = list(map(int,input()))
#         arr.append(a)
#
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 3:
#                 sr = i
#                 sc = j
#     print("#{} {}".format(tc, find()))

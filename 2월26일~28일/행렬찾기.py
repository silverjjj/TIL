'''
9
1 1 3 2 0 0 0 0 0
3 2 5 2 0 0 0 0 0
2 3 3 1 0 0 0 0 0
0 0 0 0 4 5 5 3 1
1 2 5 0 3 6 4 2 1
2 3 6 0 2 1 1 4 2
0 0 0 0 4 2 3 1 1
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
'''

def find(x,y):
    global case
    global result
    dx = [0, 1]
    dy = [1, 0]  #오 아래
    sero = 0
    sx = x
    sy = y
    nx = x
    ny = y
    # for i in range(2):
    #     nx = x + dx[i]
    #     ny = y + dy[i]
    while visited[nx][ny] != 1 and case[nx][ny] != 0:
        sero +=1
        garo = 0
        while visited[nx][ny] != 1 and case[nx][ny] != 0:
            visited[nx][ny] = 1
            garo +=1
            nx = nx + dx[0]     # 오른쪽으로 ㄱ
            ny = ny + dy[0]
            visited[nx][ny] = 1
        nx = sx + dx[1]*sero #아래로 ㄱㄱ
        ny = sy + dy[1]*sero


    print(visited)
    # result.append(sero,garo)


    return print(sero,garo)
    # s = []
    # arr[y][x] = 0
    # while len(s) != 0:
    #     for i in range(2): # 먼저 오른쪽부터,
    #         ny = y + dy[i]
    #         nx = x + dx[i]
    #         s.append([y, x])
    #         n = s.pop()
    #         # if 0<=nc<N and 0 <=nr<N:
    #         #     k=1
    #         while case[ny][nx] != 0:
    #             s.append([ny,nx])
    #             arr[ny][nx] = 0
    #             n = s.pop()
    #             ny = n[0] + dy[i]
    #             nx = n[1] + dx[i]


N = int(input())
case = []
result= []
visited = [[0]*N for _ in range(N)]
# for a in visited:
#     print(a)
for _ in range(N):
    arr = list(map(int, input().split()))
    case.append(arr)
# for row in case:
#     print(row)
for i in range(N):
    for j in range(N):
        if visited[i][j] != 1 and case[i][j] != 0:      # 방문하면 1로 표시
            find(i,j)
            # print(result)

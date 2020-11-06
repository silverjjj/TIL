# 1258

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

4
1 2 0 0
0 0 0 0
9 4 2 0
1 7 3 0
'''
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def find(x,y):
    global sunse,xy
    s = []
    s.append([x,y])
    while s:
        sx,sy = s.pop()
        for k in range(3):
            nx = sx+dx[k]
            ny = sy+dy[k]
            if 0<=nx<n and 0<=ny<n and visit[nx][ny] ==0 and arr[nx][ny] !=0:
                visit[nx][ny]=1
                s.append([nx,ny])
    # 행(x),열(y) 측정

    for r in visit:
        print(r)
    sero =0
    garo =0

    tmpx = x
    while visit[x][y] == 1 and 0<=x<n:
        x += 1
        sero+=1
        if not 0<=x<n:
            break
    while visit[tmpx][y] == 1:
        y+=1
        garo+=1
        if not 0<=y<n:
            break
    # print(sero,garo)
    sunse.append(sero*garo)
    xy.append([sero,garo])
# T = int(input())
# for tc in range(1,T+1):
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
visit = [[0]*n for _ in range(n)]
minV = 123456

sunse = []
xy = []
result = 0
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0 and arr[i][j] != 0:
            find(i,j)

            # result = sero*garo
            # sunse.append([result,sero,garo])

print(sunse)
print(xy)
# 정렬하는걸 못하겠다.

# for i in range(len(sunse)):

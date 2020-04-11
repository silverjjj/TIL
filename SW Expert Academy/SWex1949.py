# SWex1949. [모의 SW 역량테스트] 등산로 조성


def dfs(x,y):
    global maxV
    dx = [-1, 1, 0, 0]  # 상하좌우
    dy = [0, 0, -1, 1]
    s = []
    cnt = 0
    s.append((x,y))
    while s:
        print(s)
        sx,sy = s.pop()
        re = True
        for i in range(4):
            nx = sx + dx[i]
            ny = sy + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if rm[sx][sy] > rm[nx][ny]:
                    s.append((nx,ny))
                    cnt +=1
                    break
                # 이동할 위치가 전 위치보다 크거나 같을경우엔 k범위 내에서 빼준다.
                elif re == True:
                    for kk in range(1,k+1):
                        # 1~ k범위에서 새로운 위치에 빼서 가장 큰 경우의수로
                        if rm[sx][sy] > rm[nx][ny]-kk:
                            s.append((nx,ny))
                            cnt +=1
                            re = False # k는 한번만 사용한다
                            break
                    break
    return cnt


n,k = map(int,input().split())
rm = [list(map(int,input().split())) for _ in range(n)]
maxV = 0
cnt = 1
# 가장 큰 높이를 알기위한 알고리즘
for i in rm:
    if max(i) > maxV:
        maxV = max(i)
print(maxV)
for x in range(n):
    for y in range(n):
        if rm[x][y] == maxV:
            print(dfs(x,y))


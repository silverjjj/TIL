# SWex1949. [모의 SW 역량테스트] 등산로 조성
'''
가장 큰수의 위치를 찾는다.
그 위치를 중심으로 상 하 좌 우 를 이동, 이땐 큐를 사용 그리고 이동중
값이 크거나 같을때 k범위내에서 지형을 깍을수있다. (k가 아무리 커도 현 위치의 -1크기로)
만약 옆에 1일경우 이것도 - 가능
'''
dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]
def dfs(x,y):
    global maxV
    q = []
    flag = 0
    cnt = 0
    q.append((x,y))
    while q:
        sx,sy = q.pop(0)
        for k in range(4):
            nx = sx + dx[k]
            ny = sy + dy[k]
            if 0<=nx<n and 0<=ny<n:
                if rm[sx][sy] > rm[nx][ny] and 1 >= flag:
                    q.append((nx,ny))
                    
                else:
                    flag += 1
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


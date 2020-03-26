def virus(tmp):                                 # 3개의 벽이 조합으로 정해진 tmp에 바이러스를 퍼지게 하기 위한 함수
    dx = [-1,1,0,0]# 상하좌우
    dy = [0,0,-1,1]
    s = []

    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 2:              # tmp에서 바이러스 3개를 찾아 s에 푸쉬하자
                s.append((i,j))

    while len(s) != 0:                      # s가 비어있을떄까지 돌린다. len(s) == 0이되면 빠져나감
        sx,sy = s.pop()                     # 바이러스의 위치 3개중 한개를 pop해서
        for k in range(4):                  # 그 4주변을 돌리자 상 > 하 > 좌 > 우
            nx = sx + dx[k]
            ny = sy + dy[k]
            if 0<=nx<n and 0<=ny<m and tmp[nx][ny] == 0:        #tmp[nx][ny] == 0 의 의미 -> 바이러스(2)에 4면중 0인부분에
                tmp[nx][ny] = 2                                 # 바이러스를 감염시키고
                s.append((nx,ny))                               # 감염된 위치를 다시 s에 푸쉬
                                                                #이러한 과정을 계속해서 반복하자 !! 언제까지?? s가 비어질때까지


def comb(visit,idx,cnt): # 벽의 위치를 1차원배열로 표현, 벽의 위치, 벽의갯수
    global maxV
    if cnt == 3:                            # 벽의 갯수가 3개가 되면
        tmp = [i[:] for i in rm]            # 처음 기준인 rm을 tmp로 복사 why? rm을 갖고 쓰면 복잡해짐. rm을 일시적으로 2차원배열 tmp에 넣어서 tmp를 이용하자

        for j in range(len(visit)):         #벽의 위치를 찾자
            if visit[j] ==1:
                r = j // m                  # 1차원 배열인 visit에서 찾은 벽의 위치를 2차원배열로 표현하기 위해 이러한 방법을 사용
                c = j % m
                tmp[r][c] = 1               # 2차원 배열인 tmp에 벽의 위치를 표현
        virus(tmp)                          # 3개의 벽을 정한 tmp를 바이러스 함수로 보낸다

        safe = 0                            # 바이러스에 감염된후 tmp에서의 0(감염안된 빈방)의 갯수를 찾자
        for r in range(n):
            for c in range(m):
                if tmp[r][c] == 0:
                    safe +=1
        # print(safe)
        if safe > maxV:                     # 실시간으로 maxV와 비교하며 max값을 찾는다.
            maxV = safe
        return

    if idx == len(visit):                    # 계속 comb함수가 돌다가 idx가 맨 마지막까지 도달하면 return
        return

    # 1을 설정
    x = idx // m                # 1차원 배열의 벽의 위치인 idx를 2차원으로 표현
    y = idx % m
    if rm[x][y] == 0:           # rm[x][y] == 0 은 rm에서 1과 2를 제외한 빈공간에만 벽을 설치하기위해
        visit[idx] = 1          # 벽을 설치함 > 이때 visit(1차원 배열) 을 이용
        comb(visit,idx+1,cnt+1) # 벽을 설치한뒤 다시 comb로 보내 다음 벽을 설치하자
    visit[idx] = 0              # 만약에 rm[x][y]이 1 or 2 일땐 벽을 설치할필요가 없으니 visit[idx] = 0으로 하자
    comb(visit, idx + 1, cnt)   # 다음칸에 가기위해 idx+1을 하지만 벽은 설치하지 않았으니 cnt+0이다

n,m = map(int,input().split())
rm = [list(map(int,input().split())) for _ in range(n)]
visit = [0] * (n * m)    # 벽의 visit을 1차원배열로 정의
maxV = 0
comb(visit,0,0)     # 벽, visit의 idx, cnt(벽의 설치)
print(maxV)
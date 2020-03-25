T = int(input())
for tc in range(1,T+1):
    n = int(input())
    rm = [[0]*n for _ in range(n)]
    num = 1
    rm[0][0] = 1
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    # 오 아래 왼 위
    tmpx = tmpy = 0
    while num < n**2:
        for k in range(4):
            nx = tmpx + dx[k]
            ny = tmpy + dy[k]
            while 0<=nx<n and 0<=ny<n:
                if rm[nx][ny] == 0:
                    num += 1
                    rm[nx][ny] = num
                    # print(rm)
                    tmpx =nx
                    tmpy =ny

                    nx = tmpx + dx[k]
                    ny = tmpy + dy[k]
                    # print(nx,ny)
                else:
                    break
    print("#{}".format(tc))
    for i in range(n):
        for j in range(n):
            print(rm[i][j], end = " ")
        print()


# 문제2 희토류를 찾아라
'''
5
0 1 1 2 1
1 1 1 2 0
1 0 1 1 2
2 1 1 0 2
1 2 1 0 2
'''
T = int(input())
for tc in range(1,T+1):
    def f(x,y):
        global visit,cnt,rm
        visit[x][y] = 1    # 함수에 들어오지마자 방문을 표시
        dx = [-1,-1,-1,0,1,1,1,0]       #총 8면을 알아보기 위한 dx와 dy값
        dy = [-1,0,1,1,1,0,-1,-1]
        s = []
        s.append((x,y))     # 들어온 좌표 x,y를 스택에 넣는다
        while s:
            sx,sy = s.pop()     # while문에 들어오지마자 스택을 pop하고 sx,sy에 할당한뒤 sx,sy부터 시작
            for k in range(8):  # 8면을 알아보기 위한 for문
                nx = sx + dx[k]
                ny = sy + dy[k]
                if 0<=nx<n and 0<=ny<n and visit[nx][ny] == 0 and rm[sx][sy] == rm[nx][ny]:
                    # 배열안에 있고 방문하지 않아야한다. 그리고 희토류 지도인 rm에서 이동전 위치인 sx,sy와 이동한 위치인 nx,ny와 같아야만 방문한다.
                    visit[nx][ny] = 1       # 위 조건에 해당하면 방문
                    cnt +=1                 # cnt를 +1해준다
                    s.append((nx,ny))       # 이동한 위치를 다시 스택에 push 해준다.
        # 위 과정을 계속해서 반복하면서 빈 스택일경우 while문을 빠져나간다.

    n = int(input())
    rm = [list(map(int,input().split())) for _ in range(n)]     # n*n면적의 희토류 지도
    visit = [[0] * n for _ in range(n)]     # 방문할때마다 1을 표시하기 위한 2차원 배열
    maxV = 1
    sum = size = 0
    for i in range(n):
        for j in range(n):
            if rm[i][j] != 0 and visit[i][j] == 0:  # 희토류 지도에 광맥이 있고 방문하지 않았을경우에만 함수로 이동
                cnt = 1                             # 함수에 들어가서 갯수파악을 위한 cnt
                f(i, j)                             # f 함수
                sum = cnt * rm[i][j]            # 함수에서 나와 cnt * rm[i][j]를 하여 총 매장량을 알아내자
                if sum > maxV:                  # maxV값과 비교하여 sum이 maxV보다 maxV값을 다시 정의
                    maxV = sum
                    size = sum // rm[i][j]      # 광맥의 size(면적)를 알기위한 계산
    print("#{} {} {}".format(tc, maxV, size))



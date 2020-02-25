def find():
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    s = []
    s.append([sr,sc])       # start 지점을 스택에 쌓는다.
    arr[sr][sc] = 1         # 다시 되돌아오지 못하게 1로 막아놓는다.
    while len(s) != 0:
        n = s.pop()
        for i in range(4):      # 4방탐색을 통해 0을 찾는다.
            nr = n[0] + dr[i]       # nr은 new row
            nc = n[1] + dc[i]
            if 0<= nr < N and 0<=nc<N:
                if arr[nr][nc] == 2:
                    return 1
                elif arr[nr][nc] == 0:
                    s.append([nr,nc])
                    arr[nr][nc] = 1
    return 0
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = []
    for i in range(N):
        a = list(map(int,input()))
        arr.append(a)

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                sr = i
                sc = j
    print("#{} {}".format(tc, find()))

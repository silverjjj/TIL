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
def find(x,y):
    dx = [0,1]  # 오른/아래
    dy = [1,0]
    sx = x
    sy = y
    nx = x
    ny = y
    garo = sero = 0
    #세로찾기
    while case[nx][ny] != 0 and visited[nx][ny] == 0:
        #가로찾기
        garo = 0
        while case[nx][ny] != 0 and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            nx = nx + dx[0]
            ny = ny + dy[0]
            garo +=1
            if 0 > nx or nx >= n or 0 > ny or ny >= n:
                break

        nx = sx + dx[1] +dx[1]*sero
        ny = sy + dy[1] +dy[1]*sero
        sero+=1
        if 0 > nx or nx >= n or 0 > ny or ny >= n:
            break
    return [sero, garo, sero*garo]

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    case = []
    result = []
    a = []
    re = []
    sum = 0
    for _ in range(n):
        arr = list(map(int, input().split()))
        case.append(arr)
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and case[i][j] != 0:
                a.append(find(i,j))

    n = len(a)
    # 크기순서대로 다시 배열
    for i in range(n-1):
        for j in range(n-1-i):
            if a[j][-1] > a[j+1][-1]:
                a[j],a[j+1] = a[j+1],a[j]
            elif a[j][-1] == a[j+1][-1] and a[j][0] > a[j+1][0]:
                a[j], a[j + 1] = a[j + 1], a[j]

    print("#{} {}".format(tc,n), end = " ")
    for i in range(n):
        print("{} {}".format(a[i][0],a[i][1]), end = " ")
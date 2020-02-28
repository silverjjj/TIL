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
    return [sero, garo,sero*garo]

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    case = []
    result = []
    stan = []
    a = []
    for _ in range(n):
        arr = list(map(int, input().split()))
        case.append(arr)
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and case[i][j] != 0:
                result.append(find(i,j))
    print(result)
    for i in range(len(result)):
        stan.append(result[i][-1])
    stan.sort()
    print(stan)
    for i in range(len(stan)):
        for j in range(len(result)):
            if stan[i] == result[j][0]*result[j][1]:
                a.append(result[j][0])
                a.append(result[j][1])
                # stan.remove(stan[i])
                # stan.insert(i,0)
    a = list(map(str,a))
    a = " ".join(a)
    num = len(result)
    print("#{} {} {}".format(tc,num,a))
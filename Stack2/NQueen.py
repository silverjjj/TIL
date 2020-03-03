def nqueen(x):
    global cnt

    if x == n:
        cnt +=1
        return

    for y in range(n):
        if visited[y] == 0:
            for i in range(x):
        visited[level] = i
        nqueen(level+1)



T = int(input())
for tc in range(1,T+1):
    n = int(input())
    cnt = 0
    visited = [0]*n     # 행의 열정보 저장
    nqueen(0)

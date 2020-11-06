# SWex6057. 그래프의 삼각형
T = int(input())
result = []
for tc in range(T):
    n, m = map(int, input().split())
    rm = [[0] * (n + 1) for _ in range(n + 1)]
    cnt = 0
    for _ in range(m):
        x, y = list(map(int, input().split()))
        rm[x][y] = 1
        rm[y][x] = 1
    for i in range(1, n + 1):
        for j in range(i+1, n + 1):
            for k in range(j+1, n + 1):
                if rm[i][j] == rm[i][k] == rm[j][k] == 1:
                    cnt += 1
    result.append(cnt)
for tc in range(T):
    print("#{} {}".format(tc+1,result[tc]))
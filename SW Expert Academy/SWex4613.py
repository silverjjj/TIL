def f(i,j,k):
    global cnt
    global minV
    for r in range(0, i):
        for c in range(m):
            if case[r][c] != 'W':
                # case[r][c] = 'W'
                cnt += 1

    for r in range(i, i + j):
        for c in range(m):
            if case[r][c] != 'B':
                # case[r][c] = 'B'
                cnt += 1

    for r in range(i + j, i + j + k):
        for c in range(m):
            if case[r][c] != 'R':
                # case[r][c] = 'R'
                cnt += 1

    if cnt < minV:
        minV = cnt
    return minV

T= int(input())
for tc in range(1,T+1):
    n, m = map(int,input().split())
    case = [list(input()) for _ in range(n)]
    # print(case)
    # print(case[0][0])
    minV = 987654321
    row = 0
    cnt = 0
    cnt_list = []
    for i in range(1,n):
        for j in range(1,n):
            for k in range(1,n):
                if i+j+k == n:
                    cnt = 0
                    f(i,j,k)

    print("#{} {}".format(tc,minV))
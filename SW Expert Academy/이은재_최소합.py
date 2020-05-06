def min_sum(x,y,s):
    global minV
    if x == n-1 and y == n-1:   # 도착지에 도착하면
        if minV > s+rm[x][y]:
            minV = s+rm[x][y]
    elif minV < s+rm[x][y]:     # 계산하다가 minV값을 넘어서면 리턴
        return
    else:
        # 아래 이동
        if 0 <= x < n-1:
            min_sum(x+1, y, s+rm[x][y])
        # 우측 이동
        if 0 <= y < n - 1:
            min_sum(x, y+1, s+rm[x][y])
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    rm =[list(map(int, input().split())) for _ in range(n)]
    minV = 123456789
    min_sum(0,0,0)
    print("#{} {}".format(tc,minV))
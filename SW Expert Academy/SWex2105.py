# #2105. [모의 SW 역량테스트] 디저트 카페 - 백트래킹으로 품

dx = [1, 1, -1, -1] # k = 0 , 1 , 2 , 3 가자
dy = [1, -1, -1, 1] # 위치 우하,좌하,좌상,우상 기준방향은 시계방향
def dessert(x,y,k,nums):
    global ans
    # 범위 넘어가면 리턴
    # if x >= n or y >= n or x < 0 or y < 0:
    #     return
    # k가 넘어가면 리턴
    # if k >= 4:
    #     return

    if 0<=x<n and 0<=y<n and k <= 3:
        if k == 3 and arrive_x ==x and arrive_y ==y:
            # print(len(nums))
            if len(nums) > ans:
                ans = len(nums)
                return
        if rm[x][y] in nums:
            return
        # 계속 한방향으로 ,nums+[rm[x][y]]
        dessert(x+dx[k],y+dy[k],k,nums+[rm[x][y]])
        # 계속 한방향으로 가다가 도저히 갈곳이 없다면, 꺾는 방향으로
        dessert(x+dx[k],y+dy[k],k+1,nums+[rm[x][y]])
    else:
        return


T = int(input())
for tc in range(1,T+1):
    n = int(input())
    rm = [list(map(int,input().split())) for _ in range(n)]
    ans = -1
    for i in range(0,n-1):
        for j in range(1,n-1):
            arrive_x = i
            arrive_y = j
            nums = []
            dessert(i,j,0,nums)
        if ans == 4+(n-3)*2:
            break
    print("#{} {}".format(tc,ans))




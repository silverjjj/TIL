def bus(num):
    global minV,cnt
    # print(num, minV)
    if num >= n:
        if minV > cnt:
            minV = cnt
        return
    if cnt >= minV:  # 중간 자르기
        return
    start = num          # 새로운 시작점
    end = arr[num]+num
    for i in range(end,start,-1):
        # i = > 가장 멀리 ~ 가장 가까이있는 num
        cnt +=1
        bus(i)
        cnt -=1
T = int(input())
for tc in range(1,T+1):
    charge = list(map(int,input().split()))
    n = charge[0] -1    # 0~ 9
    arr = charge[1:]
    minV = 100000
    cnt = 0
    bus(0)
    print("#{} {}".format(tc,minV-1))
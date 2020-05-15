# 백트래킹을 이용한 SWex 문제
def bus(num):
    global minV,cnt
    if num >= n:            # 목표도달
        if minV > cnt:
            minV = cnt
        return
    if cnt >= minV:       # 가지치기
        return
    start = num
    end = arr[num]+num
    # i = > 가장 멀리 ~ 가장 가까이있는 num
    for i in range(end,start,-1):       # promising한 부분
        cnt +=1
        bus(i)
        cnt -=1

T = int(input())
for tc in range(1,T+1):
    charge = list(map(int,input().split()))
    n = charge[0] - 1
    arr = charge[1:]
    minV = 100000
    cnt = 0
    bus(0)
    print("#{} {}".format(tc,minV-1))
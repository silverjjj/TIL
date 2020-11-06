#SWex5099. [파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기
T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    ci = list(map(int,input().split()))
    bin = []
    for i in range(m):
        bin.append([ci[i],i+1])
    pan = []
    for i in range(n):
        tmp = bin.pop(0)
        pan.append(tmp)
    while len(pan) != 1:
        pan[0][0] = pan[0][0] // 2
        if pan[0][0] != 0:
            tmp = pan.pop(0)
            pan.append(tmp)
        elif pan[0][0] == 0:
            pan.pop(0)
            if len(bin) != 0:
                tmp = bin.pop(0)
                pan.append(tmp)
    print("#{} {}".format(tc,pan[0][1]))
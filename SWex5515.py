T = int(input())
for tc in range(1,T+1):
    M,D = map(int, input().split())
    day = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    if M == 1:
        sum = 0
    else:
        sum = 31
        for i in range(2,M):
            if i >= 2 :
                sum += day[i]
    sum +=D
    sum -=4
    result = sum%7
    print('#{} {}'.format(tc,result))
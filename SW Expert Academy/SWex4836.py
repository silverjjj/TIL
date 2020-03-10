# SWex 4836. [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기

for tc in range(1,1+int(input())):
    n = int(input())
    room = [[0] * 10 for _ in range(10)]
    cnt = 0
    for i in range(n):
        x1,y1,x2,y2,c = map(int,input().split())
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                room[i][j] +=c

    for i in range(10):
        for j in range(10):
            if room[i][j] >= 3:
                cnt +=1
    print("#{} {}".format(tc,cnt))
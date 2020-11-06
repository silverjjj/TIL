# SWex3349. 최솟값으로 이동하기
for tc in range(int(input())):
    w,h,n = map(int,input().split())
    x=[]
    y=[]
    for i in range(n):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    cnt = 0
    for i in range(n-1):
        # print(x[i],x[i+1],y[i],y[i+1])
        if (x[i] < x[i+1] and y[i] < y[i+1]) or (x[i] > x[i+1] and y[i] > y[i+1]):
            cnt += max(abs(x[i] - x[i+1]), abs(y[i] - y[i+1]))
        else:
            cnt += abs(x[i] - x[i+1]) + abs(y[i] - y[i+1])
    print("#{} {}".format(tc+1,cnt))
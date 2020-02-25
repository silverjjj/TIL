for tc in range(1,1+int(input())):
    N, M = map(int,input().split())
    u = 0
    while N - 2*u != M - 1*u:
        u+=1
    print("#{} {} {}".format(tc,M-u,u))
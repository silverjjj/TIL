T = input(int())
for tc in range(1,T+1):
    a,b = map(str,input().split())
    n = len(a)
    m = len(b)
    i = 0
    cnt = 0
    while i < n:
        if a[i:i+m] == b and i<=n-m:
            cnt +=1
            i+=m
        else:
            cnt+=1
            i+=1

    print('#{} {}'.format(tc, cnt))
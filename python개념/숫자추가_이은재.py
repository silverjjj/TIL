T = int(input())
for tc in range(1,T+1):
    n,m,l = map(int,input().split())
    rm = list(map(int,input().split()))
    for _ in range(m):
        a,b = map(int,input().split())
        rm.insert(a,b)
    print("#{} {}".format(tc,rm[l]))
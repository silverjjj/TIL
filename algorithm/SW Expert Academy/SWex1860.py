T = int(input())
for tc in range(1,T+1):
    n,m,k = list(map(int,input().split()))
    p = list(map(int,input().split()))
    p.sort()
    result = 'possible'
        


    num = []

    for i in range(n):
        if p[i] % m <= k:

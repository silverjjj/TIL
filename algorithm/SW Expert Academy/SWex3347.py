for tc in range(1, int(input())+1):
    N,M = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    total =[]
    cnt = []
    for i in range(M):
        for j in range(N):
            if b[i]>=a[j]:
                total.append(a[j])
                break
    for k in range(len(total)):
        cnt.append(total.count(total[k]))
    # print(total)
    # print(cnt)
    num = cnt.index(max(cnt))
    print("#{} {}".format(tc,a.index(total[num])+1))

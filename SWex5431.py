for tc in range(1,int(input())+1):
    N,k = list(map(int,input().split()))
    num = list(map(int,input().split()))
    a = []
    for i in range(1, N+1):
        a.append(i)
    sum = a + num
    cnt =[]
    for i in range(len(sum)):
        cnt.append(sum.count(sum[i]))
    result = []
    for i in range(len(sum)):
        if cnt[i] == 1:
            result.append(sum[i])
    result = " ".join(map(str,result))
    print("#{} {}".format(tc,result))
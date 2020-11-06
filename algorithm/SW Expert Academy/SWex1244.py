# SWex1244 최대 상금
def find(num,k):
    global maxV,max_result
    if maxV == max_result:
        maxV = max_result
        return
    if k == K:
        str_num = list(map(str,num))
        int_num = int(''.join(str_num))
        if int_num > maxV:
            maxV = int_num
        return

    for i in range(len(num)-1):
        for j in range(i+1, len(num)):
            num[i], num[j] = num[j], num[i]
            if num[:] not in num_list[k]:
                num_list[k].append(num[:])
                find(num,k+1)
            num[j], num[i] = num[i], num[j]

T = int(input())
for tc in range(1,T+1):
    n, K = list(map(int,input().split()))
    num = []
    maxV = 0
    while n:
        last = n % 10
        num.append(last)
        n = n // 10
    max_result = int("".join(list(map(str,reversed(sorted(num))))))
    num.reverse()
    num_list = [[] for i in range(K)]
    find(num,0)
    print("#{} {}".format(tc,maxV))

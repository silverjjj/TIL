# SWex5642. [Professional] 합
T = int(input())
sum_list = []
for tc in range(T):
    n = int(input())
    num = list(map(int,input().split()))
    maxV = 1
    # for i in range(n):
    #     sum = 0
    #     for j in range(i,n):
    #         print(num[j],end=" ")
    #     print()
    # print()
    for k in range(n):
        for i in range(k,n):
            sum = 0
            for j in range(k,i+1):
                # print(num[j],end=" ")
                sum += num[j]
                print(num[j],end = " ")
            print()
            print("합 : ", sum)
            if sum>maxV:
                maxV =sum
        print()
    #         print()
    #     print()
    # print()
    #         sum += num[j]
    #         if sum > maxV:
    #             maxV = sum
    print("#{} {}".format(tc + 1, maxV))
#     sum_list.append(maxV)
# for tc in range(T):
#     print("#{} {}".format(tc+1, sum_list[tc]))
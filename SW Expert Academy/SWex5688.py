# SWex5688. 세제곱근을 찾아라
for tc in range(int(input())):
    n = int(input())
    cnt = 0
    result = -1
    for i in range(10**6+1):
        print(i)
        if n==i**3:
            result = i
            break

    print("#{} {}".format(tc+1,result))
    # result = 0
    # x = round(n**(1/3),0)
    # if x**3 == n:
    #     result = x
    # else:
    #     result = -1
    # result = int(result)
    # print("#{} {}".format(tc+1,result))
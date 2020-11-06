# SWex1225
for _ in range(10):
    tc = int(input())
    arr = list(map(int,input().split()))
    re = True
    while re:
        # print(arr)
        for i in range(1,6):
            arr[0]-=i
            tmp = arr.pop(0)
            arr.append(tmp)
            if tmp <= 0:
                re = False
                break
    arr[-1] = 0
    result = ""
    for j in range(len(arr)):
        result += (str(arr[j])+" ")
    print("#{} {}".format(tc,result))

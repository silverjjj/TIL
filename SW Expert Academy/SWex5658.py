# SWex5658 보물상자 비밀번호
T = int(input())
for tc in range(1,T+1):
    n,k = map(int,input().split())
    num = input()
    unit = n//4
    num_list = []
    cnt = unit
    while cnt > 0:
        cnt -=1
        if type(num) == list:
            num = ''.join(num)

        for i in range(0,n+1-unit,unit):
            if num[i:i + unit] not in num_list:
                num_list.append(num[i:i + unit])
        # print(num_list)
        num = list(num)
        tmp = num.pop()
        num.insert(0,tmp)

    num_list.sort(reverse=True)
    # print(num_list)
    num16 = num_list[k-1]
    num10 = int(num16,16)
    print("#{} {}".format(tc,str(num10)))
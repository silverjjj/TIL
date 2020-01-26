T = int(input())
count = 0
for test_case in range(1,T+1):
    while T > count:
        count +=1
        num = list(map(int,input().split()))
        if len(num) == 10:
            num.sort()
            result =0
            for i in range(1,9):
                result += num[i]
        print(f"#{count}",round(result/8))


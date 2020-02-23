T = int(input())
count=0
while T >= count:
    for test_case in range(1,T+1):
        count +=1
        num = list(map(int,input().split()))
        num.sort()
        result =0
        for i in range(1,9):
            result += num[i]
        print(f"#{test_case}",round(result/8))
    break


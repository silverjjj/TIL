
nums = []
for _ in range(1,1+int(input())):
    n = str(input())
    while len(n) != 1:
        sum = 0
        for i in range(len(n)):
            sum += int(n[i])
        n = str(sum)
    # print(n)
    nums.append(n)
    # print(nums)
tc = 0
# 시간 딜레이 뜰때는 이렇게 리스트에 답을 추가해사 출력해낸다.
for i in nums:
    tc +=1
    print("#{} {}".format(tc,i))
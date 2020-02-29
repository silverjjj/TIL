for tc in range(1, 11):
    N = int(input())
    nums = []
    for i in range(N):
        num = list(map(int, input().split()))
        nums.append(num)
    cnt = 0
    one_cnt = 0
    for j in range(N):
        one_cnt = 0
        for i in range(N):
            if nums[i][j] == 1:
                one_cnt = 1
            elif nums[i][j] == 2 and one_cnt == 1:
                cnt +=1
                one_cnt = 0
    print("#{} {}".format(tc,cnt))
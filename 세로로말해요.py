for tc in range(1, int(input())+1):
    nums=[]
    for _ in range(5):
        nums.append(input())
    max_len = 0
    for i in range(5):                  # max_len 구하기
        if len(nums[i]) > max_len:
            max_len = len(nums[i])

    result = ""
    for j in range(max_len):         # j 0~5
        for i in range(5):
            if j < len(nums[i]):        # 이 조건이 제일 중요
                result += nums[i][j]
    print("#{} {}".format(tc,result))







T = int(input())
for test_case in range(1, T + 1):
    str_list = [[] for _ in range(5)]
    max_len = 0
    my_str = ""

    for n in range(5):
        str_list[n] = input()
        if len(str_list[n]) > max_len:
            max_len = len(str_list[n])
    print(max_len)
    for i in range(max_len):
        for j in range(5):
            if i <len(str_list[j])-1:
                my_str += str_list[j][i]

    print('#{} {}'.format(test_case, my_str))
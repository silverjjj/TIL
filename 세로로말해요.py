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
            print(i,len(str_list[j]))
            if i <len(str_list[j])-1:
                my_str += str_list[j][i]

    print('#{} {}'.format(test_case, my_str))
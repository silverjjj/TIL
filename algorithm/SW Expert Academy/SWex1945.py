T = int(input())
case = [2, 3, 5, 7, 11]
number = list()
for test_case in range(1,T+1):
    N = int(input())
    number = []
    for i in case:
        count = 0
        while N % i == 0:
            N //=i
            count += 1
        number.append(str(count))
    print('#{0} {1}'.format(test_case, ' '.join(number)))  # join : 문자열 number 사이에 ' '를 입력한다.












# T = int(input())
# # #
# # # case = [2, 3, 5, 7, 11]
# # # for t in range(1, T + 1):
# # #     N = int(input())
# # #     result = []
# # #     for i in case:
# # #         count = 0
# # #         while N % i == 0:
# # #             N //= i
# # #             count += 1
# # #         result.append(str(count))
# # #     print('#{0} {1}'.format(t, ' '.join(result)))
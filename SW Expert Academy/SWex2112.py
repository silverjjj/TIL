# SWex2112. [모의 SW 역량테스트] 보호 필름
'''
6 8 3
0 0 1 0 1 0 0 1
0 1 0 0 0 1 1 1
0 1 1 1 0 0 0 0
1 1 1 1 0 0 0 1
0 1 1 0 1 0 0 1
1 0 1 0 1 1 0 1
'''

from itertools import product, combinations


def my_func():

    for cnt in range(K):  # 0 ~ K - 1
        print("cnt : ",cnt)
        for AB in product((0, 1), repeat=cnt):
            print("AB : ",AB)
            for idx in combinations(range(D), cnt):
                print("idx : ",idx)
                for line in zip(*DATA):
                    print(list(zip(*DATA)))
                    line = list(line)
                    # 약물 주입
                    for i in range(cnt):
                        line[idx[i]] = AB[i]
                    # 결과 확인
                    for y in range(D - K + 1):
                        temp = line[y]
                        for dy in range(1, K):
                            if temp != line[y + dy]:
                                break  # 조건 미충족, 다음 y 확인
                        else:
                            # 조건 충족, 다음 x 확인
                            break
                    else:
                        # 한 줄 전체가 조건 미충족. 다른 경우의 수 확인
                        break
                else:
                    # 모두 조건 충족. 결과 출력
                    return cnt
    # 최악의 경우
    return K


T = int(input())
for test_case in range(1, 1 + T):
    D, W, K = map(int, input().split())
    DATA = [list(map(int, input().split())) for _ in range(D)]

    print('#{} {}'.format(test_case, my_func()))





#
# def find(num,tr):
#     print(num,tr)
#     for i in range(num,)
# # 조합생성
# def comb(n,r):
#     if r == 0:
#         for num in tr:
#             find(num,tr)
#     elif n < r:
#         return
#     else:
#         tr[r-1] = arr[n-1]
#         comb(n-1,r-1)
#         comb(n-1,r)
#
# D,W,K = map(int,input().split())
# film = [list(map(int,input().split())) for _ in range(D)]
# # for row in film:
# #     print(row)
# arr = [i for i in range(D)]
# comb_list = []
# tr = [0]*K
# num_list = []
# visited = [0]*K
# p = [0]*K
# comb(D,K)
# # result = 0



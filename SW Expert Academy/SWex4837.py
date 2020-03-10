# SWex4837. [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합

T = int(input())
for tc in range(1,T+1):
    # N,K = map(int,input().split())
    arr = [1,2,3,4]
    Len = len(arr)
    cnt = 0
    # 부분집합 구하기

    lst = []
    for i in range(1 << Len):       #0부터 시작해서  2의Len승 까지의 나열 \
        sub_list = []
        # print(i)
        for j in range(Len):    # j  0~ 3
            if i & (1 << j):
                print(i, j)
                sub_list.append(arr[j])
        lst.append(sub_list)
    print(lst)
    # for i in range(1<<Len):
    #     if len(lst[i]) == N:
    #         if sum(lst[i]) == K:
    #             cnt +=1
    #
    # print('#{} {}'.format(tc,cnt))
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     case = [0]*5001
#     for _ in range(N):
#         A, B = map(int,input().split())
#         for i in range(A, B+1):
#             case[i] +=1
#     P = int(input())
#     c_list = []
#     for _ in range(P):
#         c_list.append(int(input()))
#     print("#{}".format(tc) , end = " ")
#     for i in range(1,len(c_list)+1):
#         print(case[i], end = " ")
#     print()

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    AB = []
    case = []
    cnt = 0
    for _ in range(N):
        A, B = list(map(int, input().split()))
        for i in range(B - A + 1):
            AB.append(A + cnt)
            cnt += 1
        cnt = 0
    P = int(input())
    c_list = []
    for _ in range(P):
        C = int(input())
        c_list.append(C)
    score = [0] * len(c_list)
    for i in range(len(c_list)):
        for j in range(len(AB)):
            if c_list[i] == AB[j]:
                score[i] += 1
    result = list(map(str, score))
    result = " ".join(result)
    print("#{} {}".format(tc,result))

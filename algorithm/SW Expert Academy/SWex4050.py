for tc in range(1,int(input())+1):
    n = int(input())
    case = list(map(int,input().split()))
    case.sort()
    case.reverse()
    # print(case)
    total = 0
    for i, c in enumerate(case):
        # print(i,c)
        if i % 3 != 2:
            total += c
    print("#{} {}".format(tc,total))

# for tc in range(1,int(input())+1):
#     n = int(input())
#     case = list(map(int,input().split()))
#     case.sort()
#     sum_list = []
#     # print(case)
#     if n % 3 != 0:
#         v = n % 3
#         n = n - v
#         for k in range(v):
#             # print(case[0])
#             sum_list.append(case[0])
#             case.remove(case[0])
#     # print(case)
#     for i in range(0,n,3):
#         s = []
#         for j in range(i,i+3):
#             s.append(case[j])
#         a = sum(s) - min(s)
#         sum_list.append(a)
#     # print(sum_list)
#     print("#{} {}".format(tc,sum(sum_list)))

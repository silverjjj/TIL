
N = int(input())
nums = [0 for _ in range(N)]
for i in range(N):
    nums[i] = list(map(int,input().split()))
result = [0 for _ in range(N)]
for i in range(N):
    print(nums[0:][-1-i+N])
    #nums[i][0:] = result[0:][i+N-1]
print(nums)
print(result)









# def arrspin(my_list):
#     my_reverse = []
#     result = []
#     index = 0
#     my_list_transpose = [x for x in zip(*my_list)]
#     for i in range(len(my_list_transpose)):
#         my_reverse.append(list(reversed(my_list_transpose[i])))
#         result[index].append(''.join(list(reversed(my_list_transpose[i]))))
#         index +=1
#
#     return print(result)
#
# N = int(input())
# my_list = []
# for j in range(N):
#     my = list(map(str, input().split()))
#     my_list.append(my)
#
# arrspin(my_list)
#
# # arrspin(my_list)
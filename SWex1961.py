N = int(input())
maps = []
for n in range(N):
    maps.append(list(map(int, input().split())))

newarr = [[0 for _ in range(N)] for _ in range(N)]
for i in range(len(maps)):
    for j in range(len(map[i])):
        newarr[j][N-i-1] = maps[i][j]
for row in newarr:
    print(row)
maps = newarr

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
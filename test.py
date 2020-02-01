# 2번
# def q2(number):
#     a = str(number)
#     result = 1
#     for i in range(len(a)):
#         result *= int(a[i])
#     return result
# print(q2(123))
# print(q2(2020))
# print(q2(123456789))
# 3번
# def q3(fruits, add, n):
#
#     if add in fruits:
#         fruits[add] += n
#     else:
#         fruits[add] = n
#
#     return fruits
#
#
# print(q3({'apple': 1}, 'apple', 3))
# print(q3({'apple': 1}, 'banana', 1))

# 4번
# def q4(word):
#     com = 'safy'
#
#     for i in range(len(com)):
#         if com[i] in word:
#             return True
#     else:
#         return False
#
#     # for i in range(len(word)):
#     #     for j in range(len(com)):
#     #         if word[i] == com[j]:
#     #             return True
#     #             break
#     #         else:
#     #             return False
#     #             break
# print(q4('fish'))
# print(q4('united'))
# print(q4('galaxy'))

# import sys
# input = sys.stdin.readline
#
# for _ in range(int(input())):
#     n = int(input())
#     nums = []
#     for i in range(n):
#         nums.append(str(input())[:-1])
#     dict = {}
#     for num in nums:
#         num = str(num) + "*"
#         arr = dict
#         for i in num:
#             if i not in arr.keys():
#                 arr[i] = {}
#             arr = arr[i]
#
#     flag = True
#     for num in nums:
#         num = str(num) + "*"
#         arr = dict
#         for i in num:
#             if len(list(arr[i].keys())) >= 2 and "*" in list(arr[i].keys()):
#                 flag = False
#                 break
#             arr = arr[i]
#         if not flag:
#             break
#     if flag:
#         print("YES")
#     else:
#         print("NO")


# import sys
#
# def solution(sortedPhoneBook):
#     print(sortedPhoneBook)
#     for pn1, pn2 in zip(sortedPhoneBook, sortedPhoneBook[1:]):
#         print(pn1,pn2)
#         if pn2.startswith(pn1):
#             return False
#     return True
#
# if __name__ == "__main__":
#     t = int(sys.stdin.readline())
#     for _ in range(t):
#         n = int(sys.stdin.readline())
#         phoneBook = []
#         for _ in range(n):
#             phoneBook.append(sys.stdin.readline().rstrip())
#         if solution(sorted(phoneBook)):
#             print("YES")
#         else:
#             print("NO")

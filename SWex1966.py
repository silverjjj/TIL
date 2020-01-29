# N = int(input())
# x = N / 10          # 10의 자리
# y = N % 10          # 1의 자리
# for i in range(1,N+1):
#     x = i / 10      # 입력값의 10의 자리
#     y = i % 10      # 입력값의 1의 자리
#     if x % 3 == 0 or x % 6 == 0 or x % 9 == 0:
#         print("-",end=" ")   # 10의자리가 369의 배수일경우 -로 출력
#     elif x % 3 != 0 or x % 6 != 0 or x % 9 != 0:
#         print(i, end = " ")a=int(input())
# # my_str="1"
# # for i in range(2, a+1):
# #     cnt=0
# #     for j in range(0,len(str(i))):
# #         if str(i)[j]=='3' or str(i)[j]=='6' or str(i)[j]=='9':
# #             cnt+=1
# #     if cnt==0:
# #         my_str+=" "+str(i)
# #     else:
# #         my_str+=" "+'-'*cnt
# # print(my_str)
#     elif y % 3 == 0 or y % 6 == 0 or y % 9 == 0:
#         print("-",end=" ")
#     elif y % 3 != 0 or y % 6 != 0 or y % 9 != 0:
#         print(i, end=" ")
#
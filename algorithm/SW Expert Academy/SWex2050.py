'''
알파벳으로 이루어진 문자열을 입력 받아
각 알파벳을 1부터 26까지의 숫자로 변환하여 출력하라.
[제약 사항]
문자열의 최대 길이는 200이다.
[입력]
알파벳으로 이루어진 문자열이 주어진다.
[출력]
각 알파벳을 숫자로 변환한 결과값을 빈 칸을 두고 출력한다.
'''


x=list(input())
for i in range(0,len(x)):
    print(ord(x[i])-64,end=" ")






# al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# count = -1
# count2 = -1
# for i in range(0,len(al)):
#     if i <= 8:
#         print(chr(ord(al[i])-16) + " ", end ="")
#     elif 9 <= i <= 18:
#         count +=1
#         print("1"+f"{count}"+ " ", end="")
#     else:
#         count2 +=1
#         print("2" + f"{count2}" + " ", end="")


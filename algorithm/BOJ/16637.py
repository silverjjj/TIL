'''
70분걸림
음수최저값으로 maxV로 지정하자
'''
import sys
input = sys.stdin.readline

def result(lst):
    global maxV
    for i in range(len(lst)):
        if i % 2 == 0:
            if len(lst[i]) > 1:
                j = lst[i][1]
                if j == "+":
                    lst[i] = int(lst[i][0]) + int(lst[i][2])
                elif j == "-":
                    lst[i] = int(lst[i][0]) - int(lst[i][2])
                elif j == "*":
                    lst[i] = int(lst[i][0]) * int(lst[i][2])
    lst.pop(-1)
    res = int(lst[0])
    for k in range(1,(len(lst)//2)+1):
        if lst[2*k-1] == "+":
            res += int(lst[2*k])
        elif lst[2*k-1] == "-":
            res -= int(lst[2*k])
        elif lst[2*k-1] == "*":
            res *= int(lst[2*k])
    if res > maxV:
        maxV = res

def cal(tmp):
    lst = []
    a = A[:]
    b = B[:]
    for j in tmp:
        if j == 2:
            nums = a.pop(0)+b.pop(0)+a.pop(0)
            lst.append(nums)
        elif j == 1:
            nums = a.pop(0)
            lst.append(nums)
        lst.append(b.pop(0))
    result(lst)

def find():
    global tmp
    if sum(tmp) == L:
        cal(tmp)
        return
    if sum(tmp) > L:
        return
    for i in range(1,3):
        tmp.append(i)
        find()
        tmp.pop(-1)

N = int(input())
arr = input().strip()
A = []
B = []
maxV = -float("inf")
for i in range(N):
    if not i % 2:
        A.append(arr[i])
    else:
        B.append(arr[i])
B.append("=")
L = N//2 +1 # 숫자 갯수
tmp = []
find()
print(maxV)
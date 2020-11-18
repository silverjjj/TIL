'''
10799
python은 1초에 1천만번 계산이 가능
해당 문제는 N이 최대 10만이기때문에 10만^2 = 천억이 나옴
그래서 해당 문제의 시간복잡도는 O(N)으로 풀어야함
'''

import sys
input = sys.stdin.readline
chars = str(input().rstrip())
stack = []
res = 0
for i in range(len(chars)):
    if chars[i] == "(":
        stack.append(["(",i])
    else:
        char,idx = stack.pop()
        if i-idx == 1:
            res += len(stack)
        else:
            res += 1
print(res)
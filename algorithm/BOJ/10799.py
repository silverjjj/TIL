import sys
input = sys.stdin.readline
chars = str(input().rstrip())
s = []
lines = []
lasers = [0]*len(chars)
res = 0
for i in range(len(chars)):
    if chars[i] == '(':
        s.append('(')
    elif chars[i] == ')':
        char = s.pop()
        res += len(s)
    print(res)
import sys
input = sys.stdin.readline

def VPS(chars):
    stack = []
    for char in chars:
        if char == "(":
            stack.append(char)
        else:
            if len(stack) >= 1 and stack[-1] == "(":
                stack.pop()
            else:
                return "NO"
    if len(stack)==0:
        return "YES"
    else:
        return "NO"

N = int(input())
for _ in range(N):
    chars = str(input().rstrip())
    print(VPS(chars))
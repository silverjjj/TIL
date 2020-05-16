# 스택을 이용해 괄호 찾기
T = int(input())
for tc in range(1,T+1):
    case = input()
    s = []
    result = 1
    for i in case:
        if i =='(' or i =='{':
            s.append(i)
        elif i ==')':
            if len(s) == 0 or s.pop() != '(':
                result = 0
        elif i =='}':
            if len(s) ==0 or s.pop() != '{':
                result = 0
    if len(s) != 0:
        result = 0
    print("#{} {}".format(tc,result))
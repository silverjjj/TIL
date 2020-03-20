# SWex1218 [S/W 문제해결 기본] 4일차 - 괄호 짝짓기
for tc in range(1,11):
    n = int(input())
    case = input()
    # print(type(case))
    # print(len(case))
    s = []
    result = 0
    for i in range(n):
        if case[i] =='{' or case[i] =='[' or case[i] =='(' or case[i] =='<':
            s.append(case[i])
        else:
            if case[i] == '}':
                q = s.pop()
                if q != '{':
                    break
            if case[i] == ']':
                q = s.pop()
                if q != '[':
                    break
            if case[i] == '>':
                q = s.pop()
                if q != '<':
                    break
            if case[i] == ')':
                q = s.pop()
                if q != '(':
                    break
    if len(s) == 0:
        result = 1
    print("#{} {}".format(tc,result))
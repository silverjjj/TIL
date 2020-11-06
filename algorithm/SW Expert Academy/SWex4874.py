#SWex4874. [파이썬 S/W 문제해결 기본] 5일차 - Forth
T = int(input())
for tc in range(1,T+1):
    case = input().split()
    num = ['0','1','2','3','4','5','6','7','8','9','10']
    n = len(case)
    s = []
    result = 0
    for i in range(n):
        if case[i] in num:
            s.append(int(case[i]))
        else:
            # print(s)
            if case[i] == '.':
                break
            elif len(s) == 1:
                result = 'error'
                break
            else:
                y = s.pop()
                x = s.pop()
                if case[i] == '+':
                    result = x + y
                elif case[i] == '-':
                    result = x - y
                elif case[i] == '*':
                    result = x * y
                elif case[i] == '/':
                    result = x // y
                s.append(result)
            #     s.append(result)
            # elif case[i] =='.':
            #     if len(s)
    print("#{} {}".format(tc,result))
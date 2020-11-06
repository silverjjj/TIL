for tc in range(1,1+int(input())):
    case = list(input())
    N = len(case)
    s= []
    for i in range(N):
        if not s or s[-1] != case[i]:   #not s는 리스트 s에 아무것도 없으면 append한다.
            s.append(case[i])
        elif s[-1] == case[i]:
            s.pop()
    print("#{} {}".format(tc,len(s)))

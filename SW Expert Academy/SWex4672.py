# SWex4672
# 딕셔너리로 다시풀어보장..
for tc in range(1,1+int(input())):
    case = list(input())
    n = len(case)
    cnt = 0
    cases = []
    result = True
    for i in range(n):
        for j in range(i+1,n+1):
            cases.append(case[i:j])

    for k in range(len(cases)):
        if len(cases[k]) == 1:
            cnt +=1
        else:
            for h in range(len(cases[k])//2):
                if cases[k][h] != cases[k][-1-h]:
                    break
                cnt +=1
    print("#{} {}".format(tc,cnt))
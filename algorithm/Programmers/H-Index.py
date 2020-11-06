def sol(cit):
    # ans = 0
    cnt = 1     # 인용된 논문수
    iny = 1      # 인용된 횟수
    # print(cit)
    while cnt == iny: # 논문수랑 횟수가 같을때까지 go
        s = []
        # print(s,cnt,iny)

        for i in cit:
            if i >= iny:
                s.append(i)
            # print(s)
            if len(s) == cnt:
                iny +=1
                break
        cnt += 1
    return iny-1
cit = [3, 0, 6, 1, 5]
print(sol(cit))
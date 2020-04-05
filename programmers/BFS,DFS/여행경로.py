def find(tk):
    re = []
    gi = 100
    for st in tk:
        if st[0] not in re:
            re.append(st[0])
    n = len(re)
    # print(re)
    re.sort()
    re1=[]
    # re1 = [[] for _ in range(n)]
    for i in range(1,len(re)+1):
        re1.append([re[i-1],i])
    print(re1)
    a= []
    for i in range(len(tk)):
        for j in range(2):
            if tk[i][j] == "ICN":
                visit = [[0] * 2 for _ in range(len(tk))]
                # print(visit)
                result = []
                s = []
                s.append(tk[i][j])
                # visit[i][j] = 1
                while s:
                    # print(result)
                    v = s.pop()
                    result.append(v)
                    for i in range(len(tk)):
                        if tk[i][0] == v and visit[i][0] == 0:
                             # for i in len(re1):
                            #     if v == i[0]:
                            #         if i[1] < gi:
                            #             gi = i[1]

                        visit[i][0] =1
                        visit[i][1] = 1
                        s.append(tk[i][1])
                        # print(visit)
                            # print(s)
                            break

            a.append(result)
    return a

tk = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(find(tk))
# t = ["Psfa","CFhf","ZXDAS","AASFAS"]
# # t.sort()
# print(t[0][0] <t[1][0])
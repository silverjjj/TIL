T = int(input())
for tc in range(1,T+1):
    e,n = map(int,input().split())
    tr = [[] for _ in range(1002)]
    t = list(map(int, input().split()))
    for i in range(0,len(t),2):
        tr[t[i]].append(t[i+1])
    s = []
    visit = [0]* 1002
    visit[n]= 1
    for j in tr[n]:
        s.append(j)
        visit[j] = 1
    while s:
        st = s.pop(0)
        for l in tr[st]:
            s.append(l)
            visit[l] = 1

    print("#{} {}".format(tc,sum(visit)))
def solution(n, com):
    cnt = 0
    G = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and com[i][j] == 1:
                G[i].append(j)
    visit = [0]*n
    cnt = 0
    def find(v):
        visit[v] = 1
        s = []
        s.append(v)
        while s:
            # print(s)
            v = s.pop()
            for w in G[v]:
                if visit[w] == 1:
                    continue
                else:
                    visit[w] = 1
                    v = w
                    s.append(v)
                    # print(s,v)

    for v in range(n):
        if visit[v] == 0:
            find(v)
            cnt +=1
    return cnt
n= 3
com = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n,com))
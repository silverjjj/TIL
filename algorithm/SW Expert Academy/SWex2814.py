# SWex2814 최장경로
T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    print(G)
    for _ in range(M):
        v, w = map(int,input().split())
        G[v].append(w)
        G[w].append(v)
        print(G)
    m = []
    for i in range(1, N+1):
        visit = [0] * (N + 1)
        visit[i] = 1
        S = []
        S.append(i)
        while S:
            print("--")
            for j in G[i]:
                # print(w)
                if visit[j] ==0:
                    S.append(j)
                    visit[j] = 1
                    i = j
                elif visit[j] == 1:
                    continue
            i = S.pop()
        print(visit)
        # m.append(sum(visit))


   # print("#{} {}".format(tc,max(m)))


'''
6 5
1 4
1 3
2 3
2 5
4 6
'''
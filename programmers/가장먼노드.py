# bfs 이용 -> 거리찾기!!

def solution(n,ver):
    ans = 0
    G = [[] for _ in range(n+1)]
    visit = [0] * (n+1)
    cnt = [0] * (n+1)
    for i in range(len(ver)):
        G[ver[i][0]].append(ver[i][1])
        G[ver[i][1]].append(ver[i][0])
    q = []
    q.append(1)
    visit[1] = 1
    while q:
        v = q.pop(0)
        t = cnt[v]
        for w in G[v]:
            if visit[w] == 0:
                q.append(w)
                visit[w] = 1
                cnt[w] += t +1
    maxV = max(cnt)
    for i in cnt:
        if maxV == i:
            ans +=1
    return ans

vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
n = 6
print(solution(n, vertex))
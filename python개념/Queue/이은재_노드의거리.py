# SWex5102 노드의 거리
# queue + bfs 시간 or 이동거리 문제는 bfs로 풀자
'''
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
1 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9
'''
def bfs(rm,s):
    visit = [0] * (V + 1)  # 방문배열
    # print(visit)
    q = []
    v = s  # start지점
    q.append(v)
    visit[v] =1
    while q:
        # print(q,visit)
        v = q.pop(0)  # q내 첫번째값을 빼낸다.
        t = visit[v]
        if v == G:
            return t -1
        # cnt = visit[v]
        # if t == G:
        #     return visit[t]
        for w in rm[v]:  # t에서 들르는점을을
            if visit[w] >= 1:
                continue
            # 방문하지 않았다면,
            q.append(w)  # 이동
            visit[w] = t + 1  # 이동전 값(t)+ 1
    return 0

T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    rm = [[] for _ in range(V+1)]
    for _ in range(E):
        x,y = map(int,input().split())
        rm[x].append(y)
        rm[y].append(x)
    # print(G)
    S,G = map(int,input().split())
    print("#{} {}".format(tc,bfs(rm,S)))

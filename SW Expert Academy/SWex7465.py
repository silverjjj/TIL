#SWex7465. 창용 마을 무리의 개수
def f(t):
    global visited
    # print(visited)
    visited[t] = 1
    # print(v, end = " ")
    for w in G[t]:
        if visited[w] == 1:
            continue
        f(w)

T= int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    G = [[] for _ in range(n+1)]
    visited = [0]*(n+1)
    s=[]
    dif = -1
    cnt = 0
    for i in range(m):
        a,b = map(int,input().split())
        G[a].append(b)
        G[b].append(a)
    for i in range(1,n+1):
        f(i)
        com = sum(visited)
        if com != dif:
            cnt +=1
            dif = com
    print("#{} {}".format(tc,cnt))

def find():
    INF = float('inf')
    dist = [INF] * (V + 1)  # 가중치를 갱신하는 배열
    visited = [False] * (V + 1)
    dist[0] = 0  # 0위치엔
    cnt = 0
    # 딱 노드를 이동하면서 최소 가중치를 찾기때문에, 딱 V-1번만 loop한다
    while True:
        # 다음 위치를 찾기위해
        # 인접노드의 누적 가중치값을 비교하면서 거리가 가장 작은곳으로 이동
        u = -1
        min = INF
        for x in range(V+1):
            if not visited[x] and dist[x] < min:
                min = dist[x]
                u = x
        visited[u] = True
        cnt +=1
        if u == V:
            print(dist)
            return dist[u]
        # adj[x] : x노드의 value값
        # x 노드의 인접노드의 가중치를 갱신 or 비교 해준다.
        for end,cost in adj[u]:
            # dust[end] = 인접 노드의 누적 가중치값, dist[x]: 현재노드의 누적 가중치, cost, 현재노드와 인접노드 사이의 거리
            if dist[end] > dist[u] + cost:
                dist[end] = dist[u] + cost
T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split())
    adj = { i : [] for i in range(V)}
    for _ in range(E):
        s,e,c = map(int,input().split())
        adj[s].append([e,c])
    print("#{} {}".format(tc,find()))


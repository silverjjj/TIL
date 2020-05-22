# dist, selected 배열 준비
# 시작점 선택
# 모든 정점이 선택될때 까지
# 아직 선택되지 않고 dist값이 최소인 정점 : u
# 정점 u의 최단거리 결정
# 정점 u에 인접한 정점에 대해서 간선완화

V, E = map(int, input().split())
# 인접리스트 생성
adj = {i: [] for i in range(V)}
for i in range(E):
    s, e, c = map(int, input().split())
    adj[s].append([e, c])

INF = float('inf')
# dist, selected 배열 준비
dist = [INF] * V  # 결국, 시작점에서 각각의 정점까지 최소의 가중치값
selected = [False] * V  # 방문표시를 위한 배열
dist[0] = 0  # 시작점을 위한 설정
cnt = 0
# print(adj)
while cnt < V:
    # 현재 정점의 인접정점중 dist(가중치)가 최소인 정점찾은뒤 해당 위치를 u에 할당
    min = INF
    u = -1
    for i in range(V):
        if not selected[i] and dist[i] < min:
            min = dist[i]
            u = i
    # u를 찾은뒤 방문표시를 하자!
    selected[u] = True

    # 간선완화
    # 이동한 정점의 도착정점과 가중치를 통해 다음정점에 정의되있던 가중치와 비교하며 갱신을 진행한다.
    for w, cost in adj[u]:  # 도착정점, 가중치
        if dist[w] > dist[u] + cost:  # 다음 정점의 누적가중치 > 누적가중치 + 두 정점간 가중치
            dist[w] = dist[u] + cost  # 그렇다면 갱신한다.
    cnt += 1
# 결국 dist에는 각 시작점에서 각 정점까지의 최소 가중치(최단거리)가 있다.
print(dist)
'''
다익스트라 + 인접리스트
입력
6 11
0 1 3
0 2 5
1 2 2
1 3 6
2 1 1
2 3 4
2 4 6
3 4 2
3 5 3
4 0 3
4 5 6
'''
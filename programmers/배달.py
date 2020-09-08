'''
n개의 마을중에서 1번마을에서 k시간 이하로 배달 가능한 마을만 주문배달한다.
1번에서 k이하의 가중치인 마을 갯수를 구해라
a,b,c
a,b는 연결된 마을 c는 가중치
==> 시작정점이 있으니까 다익스트라로 사용
'''
def dijkstra(adj,N,K):
    # print(adj)
    INF = float('inf')
    visited = [False] * (N+1)
    weight = [INF] * (N+1)
    weight[1] = 0
    cnt = 0
    while cnt < N:
        minV = INF
        node = -1
        for i in range(1,N+1):
            if not visited[i] and weight[i] < minV:
                # 가장 인접한 노드와 가중치
                node = i
                minV = weight[i]
        visited[node] = True
        for next_node, w in adj[node]:
            if weight[next_node] > weight[node] + w:
                weight[next_node] = weight[node] + w
        cnt += 1
    res = 0
    for i in range(1,N+1):
        if weight[i] <= K:
            res += 1
    return res

def solution(N, road, K):
    adj = {i : [] for i in range(1,N+1)}
    for a,b,c in road:
        adj[a].append([b,c])
        adj[b].append([a,c])
    answer = dijkstra(adj,N,K)
    return answer

N = 5
road = 	[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
print(solution(N, road, K))
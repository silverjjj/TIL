'''
섬연결하기
최소비용으로 모든 섬 방문하기
mst문제
'''
import heapq
def MST(adj,n):
    visited = [False] * n
    INF = float('inf')
    weight = [INF] * n
    node = [0] * n
    hq = []
    heapq.heappush(hq,(0,0))     # 가중치, 위치
    res = 0
    while hq:
        # print(hq)
        w, node = heapq.heappop(hq)
        # print(w,node)
        if visited[node]:
            continue
        visited[node] = True
        res += w
        for next_node,w in adj[node]:
            # 방문 x and 가중치가 작을시 True
            if not visited[next_node] and weight[next_node] > w:
                weight[next_node] = w
                heapq.heappush(hq, (weight[next_node], next_node))
    print(weight)
    return res
def solution(n, costs):
    adj = { i : [] for i in range(n)}
    for cost in costs:
        start = cost[0]
        end = cost[1]
        length = cost[2]
        adj[start].append([end,length])
        adj[end].append([start,length])
    answer = MST(adj,n)
    return answer
n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
solution(n, costs)
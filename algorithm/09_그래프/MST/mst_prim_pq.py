'''
우선순위 queue : heapq
heapq은 딕셔너리의 key값을 기준으로 배열된 힙을 만들어준다
heapq.heappush(heap을 위한 list, (우선순위값, 데이터))
'''
# 딕셔너리 + 큐로 푼 문제
import heapq
V, E = map(int,input().split())
adj = { i : [] for i in range(V)}
for i in range(E):
    s,e,c = map(int,input().split())
    adj[s].append([e,c])
    adj[e].append([s,c])
print(adj)
# key, p, mst 준비
INF = float('inf')  # 무한
key = [INF]*V       # 최단거리를 기록
mst = [False] * V   # mst를 했냐? 여부의 list
pq = []
# 시작 정점 선택 : 0
key[0] = 0
num = [0]*(V+1)
# 큐에 시작 정점을 넣음 => (key, 정점인덱스)

# 우선순위 큐 => 이진합 => heapq 라이브러리 사용=>
# 우선순위 : 0, 데이터 0을 push
heapq.heappush(pq,(0,0))

result = 0
while pq:
    print(pq)
    # 최소값 찾기
    k, node = heapq.heappop(pq)
    print(k,node)
    # print(k,node)
    if mst[node]:   # mst가 true일경우 continue
        continue    # mst의 true 의미 : 이미 이자리엔 최소가중치를 했다.
    # mst로 선택
    mst[node] = True
    result +=k
    # key 갱신 => key배열/큐
    # 해당 노드에서 가중치가 가장 작은걸 데려오기 위한 for문
    for end, w in adj[node]:   # end : 도착점, wt: 가중치
        if not mst[end] and key[end] > w:
            # end자리에 가중치 w를 다시 갱신
            key[end] = w
            num[end] = node
            # 큐 갱신 => 새로운 (key,정점) 삽입 => 필요없는 원소는 스킵
            heapq.heappush(pq,(key[end], end))
print(key)
print(num)
print(mst)
print(result)


'''
입력
7 11
0 5 60
0 1 32
0 2 31
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

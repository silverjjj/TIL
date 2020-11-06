'''
우선순위 queue : heapq
heapq은 딕셔너리의 key값을 기준으로 배열된 힙을 만들어준다
heapq.heappush(heap을 위한 list, (우선순위값, 데이터))

풀이 과정
(초기 가중치는 모두 INF로설정)
1. 시작점과 인접한 모든 노드에 가중치를 할당한다.
2. 시작점의 인접 가중치중 가장 작은곳을 시작점으로 다시 이동하여 1번과정을 진행
3. 진행중에 인접한 노드에 현재 시작점의 가중치보다 크면 가중치를 변경, 아니면 변경X

=> Prim's 알고리즘은 최소 우선순위 큐에서 key값이 작은 정점을 고른후
그 정점의 인접한 간선의 가중치와 연결된 정점의 key 값을 비교해서 연결된 정점의
key 값을 갱신할지 말지를 결정하는 것을 통해 MST를 구현합니다
'''

# 딕셔너리 + 큐로 푼 문제
import heapq
V, E = map(int,input().split())
###################################
# 인접 딕셔너리 생성
###################################
adj = { i : [] for i in range(V)}
for i in range(E):
    s,e,c = map(int,input().split())
    adj[s].append([e,c])
    adj[e].append([s,c])
print('###################################')
print('인접 딕셔너리 생성!!!!!!!')
print('###################################')
print(adj)
###########초기 설정###############
# key : 가중치값을 기록
# mst : 해당 idx의 노드값이 mst냐 ?
##################################
# key, p, mst 준비
INF = float('inf')  # 무한
key = [INF]*V       # 가중치값 기록
mst = [False] * V   # mst를 했냐? 여부의 list
pq = []
# 시작 정점 선택 : 0
key[0] = 0
num = [0]*(V)
# 큐에 시작 정점을 넣음 => (key, 정점인덱스)

# 우선순위 큐 => 이진합 => heapq 라이브러리 사용=>
# 우선순위 : 0, 데이터 0을 push
heapq.heappush(pq,(0,0))
result = 0

while pq:
    print('=================================================')
    # k : 가중치값, node : 정점을 pop
    # heapq가 pop할땐 k가 가장 작은 값이 출력됨.
    print(pq)
    k, node = heapq.heappop(pq)
    print("현재 노드 ==>", node, '가중치 ==>',k)
    # 해댱 idx의 mst값이 True면 진행 xx
    if mst[node]:   # mst가 true일경우 continue
        print('현재 노드인', node,'는 이미 mst를 완료했습니다.')
        continue    # mst의 true 의미 : 이미 이자리엔 최소가중치를 했다.
    mst[node] = True
    result += k
    # key 갱신 => key배열/큐
    # 해당 노드의 인접한 노드와 가중치를 불러온다
    for end, w in adj[node]:   # end : 도착점, w: 가중치
        # 해당 노드의 mst가 False고 기존의 가중치값인 key값이 w보다 크면
        if not mst[end] and key[end] > w:
            # 새로운 정점인 idx = end에 가중치를 다시 갱신
            key[end] = w
            num[end] = node
            # 큐 갱신 => 새로운 (key,정점) 삽입 => 필요없는 원소는 스킵
            heapq.heappush(pq,(key[end], end))
print("최소 가중치",key)
print("이전의 위치",num)
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

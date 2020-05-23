'''
1
3 3
1 2 1
2 3 2
1 3 3
'''

# def make_set(x):
#     p[x] = x
#
# def find_set(x):
#     if p[x] == x: return x
#     else:
#         p[x] = find_set(p[x])
# def union_set(x,y):
#     # x,y의 대표자를 찾는다.
#     px = find_set(x)
#     py = find_set(y)
#     if rank[px] > rank[py]:
#         p[py] = px
#     else:
#         p[px] = py
#         if rank[px] == rank[py]:
#             rank[py] += 1
#
# # 1~ V번
# T = int(input())
# for tc in range(1,T+1):
#     V,E = map(int,input().split())
#     arr = [list(map(int,input().split())) for _ in range(E)]
#     # 가중치기준으로 오름차순 정렬
#     arr.sort(key=lambda x:x[2])
#     print(arr)
#     p = [0]*(V+1)
#     rank = [0]*(V+1)
#     for i in range(1,V+1):
#         make_set(i)
#     print(p)
#     result = cnt = 0
#     for i in range(E):
#         s,e,c = arr[i][0],arr[i][1],arr[i][2]
#         # start와 end 접점의 대표자가 같을경우 continue
#         if find_set(s) == find_set(e):
#             continue
#         result += c
#         union_set(s,e)
#         print(p)
#         cnt +=1
#         if cnt == V-1:
#             break
#
#     print("#{} {}".format(tc,result))

'''
우선순위 queue : heapq
heapq은 딕셔너리의 key값을 기준으로 배열된 힙을 만들어준다
heapq.heappush(heap을 위한 list, (우선순위값, 데이터))
'''
# 딕셔너리 + 큐로 푼 문제
import heapq
T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split())
    # 인접리스트를 딕셔너리를 이용하여 정의
    adj = { i : [] for i in range(1,V+1)}
    for i in range(E):
        s,e,c = map(int,input().split())
        adj[s].append([e,c])
        adj[e].append([s,c])
    # keyy, p, mst 준비
    INF = float('inf')  # 무한
    key = [INF]*(V+1)       # 실시간으로 해당 노드에서의 최단거리를 할당하는 배열
    mst = [False] * (V+1)   # mst(최단거리)를 정의했냐? 여부의 list
    pq = []

    # index = 1부터 시작하기위해 index=1에서 가중치를 0으로
    # key에 시작 정점을 넣음 => key[시작정점] = 0)
    key[1] = 0

    # 우선순위 큐 => 이진합 => heapq 라이브러리 사용=>

    # heapq.heappush(heap을 위한 list, (우선순위값, 데이터))
    # pq list에 초반 가중치 : 0과 시작을 위한 node번호: 1
    heapq.heappush(pq,(0,1))
    result = 0
    while pq:
        # print(pq)
        # k : 가중치, node: 현재 노드번호
        k, node = heapq.heappop(pq)
        # print(k,node)
        if mst[node]:   # mst가 true일경우 continue
            continue    # mst의 true 의미 : 이미 이자리엔 최소가중치를 했다.
        # mst로 선택
        mst[node] = True
        result += k
        # key 갱신 => key배열/큐
        # 해당 노드에서 가중치가 가장 작은걸 데려오기 위한 for문
        for end, w in adj[node]:   # end : 도착점, wt: 가중치
            if not mst[end] and key[end] > w:
                # end자리에 가중치 w를 다시 갱신
                key[end] = w
                # 큐 갱신 => 새로운 (key,정점) 삽입 => 필요없는 원소는 스킵
                heapq.heappush(pq,(key[end], end))
    print("#{} {}".format(tc,result))


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

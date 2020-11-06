# SWex1251. [S/W 문제해결 응용] 4일차 - 하나로
'''
환경부담금 최소가 목표로 보든 섬을 연결
환경부담금 : E*L*L

6
0 0 400 400 1000 2000
0 100 0 100 600 2000
0.3
'''
# prim방법
import heapq
T=int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[] for _ in range(N)]
    for _ in range(2):
        tmp = list(map(int,input().split()))
        for i in range(N):
             arr[i].append(tmp[i])

    E = float(input())
    INF = float('inf')  # 무한
    weights = [INF]*N       # 가중치값 기록
    visited = [False]*N
    weights[0] = 0
    pq = []
    heapq.heappush(pq,(0,0))    # 0,0 => 가중치, 시작의 idx
    result = 0
    while pq:
        weight, node = heapq.heappop(pq)    # 가중치 노드번호
        if visited[node]:
            continue
        visited[node] = True
        weights[node] = weight

        result += weight
        sx = arr[node][0]
        sy = arr[node][1]
        end = -1
        for nx,ny in arr:
            end +=1
            if [sx,sy] != [nx,ny]:  # 같은 노드는 비교 xx
                wt = ((abs(sx-nx))**2 + (abs(sy-ny))**2)*E
                if not visited[end] and weights[end] > wt:
                    weights[end] = wt
                    heapq.heappush(pq,(wt,end))

    print("#{} {}".format(tc,round(result)))

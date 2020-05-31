# SWex1251. [S/W 문제해결 응용] 4일차 - 하나로
'''
환경부담금 최소가 목표로 보든 섬을 연결
환경부담금 : E*L*L

6
0 0 400 400 1000 2000
0 100 0 100 600 2000
0.3
'''

import heapq

N = int(input())
arr = [[] for _ in range(N)]
for _ in range(2):
    tmp = list(map(int,input().split()))
    for i in range(N):
         arr[i].append(tmp[i])
E = float(input())
print(arr)


INF = float('inf')  # 무한
weights = [INF]*N       # 가중치값 기록
visited = [False]*N
weights[0] = 0

pq = []
heapq.heappush(pq,(arr[0][0],arr[0][1],0))
result = 0
while pq:
    # 시작점
    print("====================================")
    # 좌표x, 좌표y, node번호
    print(visited)
    sx, sy, node = heapq.heappop(pq)
    end = -1
    if visited[node]:
        continue
    visited[node] = True

    stan = INF
    tmp_node = tmp_x = tmp_y = 0
    end = -1
    for nx,ny in arr:   # end : 도착점, w: 가중치
        end +=1
        wt = ((abs(sx-nx))**2 + (abs(sy-ny))**2)*E
        if not visited[end] and stan > wt:
            stan = wt
            tmp_node = end
            tmp_x = nx
            tmp_y = ny
        if end == N-1:
            weights[tmp_node] = wt
            heapq.heappush(pq,(tmp_x,tmp_y,tmp_node))


print(sum(weights))


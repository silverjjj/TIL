'''
비선형구조인 그래프구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는게 중요함
이를 위해
깊이 우선탐색(DFS)
너비 우선 탐색(BFS)
를 이용
'''
'''
DFS 알고리즘
1) 시작정점 v를 결정하여 방문한다
2) 정점 v에 인접한 정점중에서
    1>방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push하고 정점 w를 방문한다.
    그리고 w를 v로 하여 다시 2>를 반복한다.
    2>방문하지 않은 정점이 없다면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 
    받은 가장 마지막 방문 정점을 v 로 하여 다시 2>를 반복한다.
3) 스택이 공백 될때까지 2)를 반복..
'''
'''
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
출력
1 2 4 6 5 7 3 
'''

# dfs를 반복과 인접리스트로 구현
# V,E = map(int, input().split())
# G = [[] for _ in range(V+1)]
# # 인접리스트를 사용
# for _ in range(E):
#     u, v = map(int,input().split())
#     G[u].append(v)
#     G[v].append(u)
# visit = [0] * (V + 1)
# v = 1
# s = []
# s.append(v)
# print(G)
# visit[v] = 1
# print(v, end=" ")
# while s:
#     # v의 방문하지 않은 인접정점을 찾는다.
#     for w in G[v]:  # v=1로시작 1와 인접한것들중 작은수부터 간다.
#         if visit[w] == 1:  # 방문했다면 통과하고 방문하지 않았다면 push한다.
#             continue
#         # v ----> w
#         # 방문하지 않았다면.
#         s.append(w)
#         # print(s)
#         visit[w] = 1
#         print(w, end=" ")  # 푸쉬후 방문표시
#         v = w  # v에서 w로 이동하는거           # 자리를 이동했으니 v=w를 통해 이동한 자리에서 다시시작
#         break
#     else:
#         # print(s)
#         # 그 이전에 방문한 정점으로
#         v = s.pop()  # 이동한 v정점에서 인접한 모든 점이 방문상태면 pop하여 그 이전자리로 다시 간다.
#

# # dfs를 재귀+인접행렬로 구현
def DFS(v):
    visited[v] = 1
    print(v, end = " ")
    for i in range(1,V+1):
        if adj[v][i] == 1 and visited[i] == 0:
            DFS(i)
V,E = map(int, input().split())
adj = [[0]*(V+1) for _ in range(V+1)]
for _ in range(E):
    u, v = map(int,input().split())
    adj[u][v] = 1
    adj[v][u] = 1
visited = [0] * (V+1)
DFS(1)
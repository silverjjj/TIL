'''
첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 마지막 노드번호 V와 간선의 개수 E가 주어진다.
다음 줄부터 E개의 줄에 걸쳐 간선의 양 끝 노드 n1, n2, 가중치 w가 차례로 주어진다.
1<=T<=50, 1<=V<=1000, 1<=w<=10, 1<=E<=1000000
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split()) # 노드갯수, 간선
    adj = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        x, y, c = map(int,input().split())
        # print(adj)
        adj[x][y] = c
        adj[y][x] = c
    INF = float('inf')
    key = [INF] * (V+1)       # 시작점을 제외한 각 배열 객체 최소의 가중치 값이 있음
    p = [-1]*V          # 시작점을 제외한 각 배열 객체에는 before 정점이 있음
    mst = [False] * (V+1)   # 시작점이 다른 정점으로 이동을 했냐?? 의 유무
    key[0] = 0          # 0 위치의 가중치는 0으로 정의, 0은 시작점이기 때문에 다른 노드에서 오는 경우가 없음
    result = 0
    cnt = 0
    while cnt < V+1:  # 다 방문하면 끝
        min = INF
        u = - 10
        ############################################################
        # 인접 정점중 가중치가 가장 낮은값 min을 찾는뒤, 해당 노드번호로 이동
        ############################################################
        for i in range(V+1):
            if not mst[i] and key[i] < min:
                min = key[i]
                u = i
        mst[u] = True
        result += min
        cnt +=1
        # 이동한 노드의 인접한 모든 가중치를 key배열에 넣는다. why?? 다음을 위해
        for j in range(1,V+1):
            if not mst[j] and adj[u][j] > 0 and key[j] > adj[u][j]:
                key[j] = adj[u][j]

    print("#{} {}".format(tc,result))
'''
3
2 3
0 1 1
0 2 1
1 2 6
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10
'''
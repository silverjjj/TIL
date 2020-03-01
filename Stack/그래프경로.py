#dfs 깊이우선탐색
'''
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6

1과 6이 연결되있으면 1로 출력

7 4
1 6
2 3
2 6
3 5
2 5

9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9

'''
def find(n, end):   # n = 1, end = 6
    visited = [0]*(V+1)
    s = []
    s.append(n)
    visited[n] = 1
    while s:
        n = s.pop()
        if n == end:
            return 1
        for j in range(1,V+1):
            if adj[n][j] == 1 and visited[j] ==0:
                s.append(j)
                visited[j] = 1
    return 0


T = int(input())
for tc in range(1,T+1):
    V, E = list(map(int,input().split()))
    adj = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        y,x = list(map(int,input().split()))
        adj[y][x] = 1
    for row in adj:
        print(row)
    v,e = list(map(int,input().split()))
    find(v,e)
    print("#{} {}".format(tc,find(v,e)))
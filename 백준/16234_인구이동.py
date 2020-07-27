'''
1. 4방향에서 갈수있는 방향이 있으면 +1
2. 해당 방향을 기준으로 최대한 갈수있는곳을 찾는다.
'''
dx = [-1,1,0,0]
dy = [0,0,1,-1]

n,r,c = map(int,input().split())
mapping = [list(map(int,input().split())) for _ in range(n)]
res = 0
flag = True
while flag:
    visited = [[0]*n for _ in range(n)]
    total = 0
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                visited[x][y] = 1
                group = set()
                group = list(group)
                group.append([x,y])
                s = [[x,y]]
                while s:
                    x,y = s.pop()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and [x,y] not in group:
                            if r<= abs(mapping[x][y] - mapping[nx][ny]) <= c:
                                group.append([x,y])
                                s.append([x,y])
                print(group)
                if len(group) >= 1:
                    res += 1
                    ingu = int(total / len(group))
                    for x,y in group:
                        mapping[x][y] = ingu
                else:
                    flag = False
                # for row in mapping:
                #     print(row)
    print(res)

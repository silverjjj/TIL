# 15683_감시
'''
1. 1~5번에 따른 딕셔너리 생성
2. 함수를 활용한 dfs
3. 재귀구조로 아래층 내려갈때 현 위치 + dict 가져간다
4. 맨 아래층 도착하면 0의 갯수를 찾아본다
'''
# 오른(0), 아래(1), 왼(2), 위(3)
dx = [0,1,0,-1]
dy = [1,0,-1,0]

direction = {1: [[0],[1],[2],[3]],
             2: [[0,2],[1,3]],
             3: [[0,3],[0,1],[1,2],[2,3]],
             4: [[0,2,3],[0,1,3],[0,1,2],[1,2,3]],
             5: [[0,1,2,3]]}
def DFS(n,depth,nums,visited):
    global minV
    # print('새로운 층 :',depth,"+++++++++++++++++++++++++++++++++++++")
    if minV == 0:
        return True

    if depth == n:
        res = 0
        print("=========================")
        for row in visited:
            print(row)
        for row in visited:
            res += row.count(0)
        if minV > res:
            minV = res
        return
    # print('depth ', depth)
    # print(x,y,d)
    # visited[x][y] += 1
    else:
        x, y, d = nums[depth]
        for arr in direction[d]:
            # arr는 진행할때의 모든 방향
            tmp = [[x,y]]
            s = []
            for k in arr:
                nx = x + dx[k]
                ny = y + dy[k]
                if 0<=nx<N and 0<=ny<M and mapping[nx][ny] in (0,1,2,3,4,5):
                    s.append([nx,ny])
                    tmp.append([nx,ny])
                    while s:
                        nx,ny = s.pop()
                        nx += dx[k]
                        ny += dy[k]
                        if 0 <= nx < N and 0 <= ny < M:
                            if mapping[nx][ny] == 6:
                                continue
                            s.append([nx,ny])
                            tmp.append([nx,ny])
            for i,j in tmp:
                visited[i][j] +=1
            if DFS(n, depth+1, nums, visited):
                return True
            for i,j in tmp:
                visited[i][j] -= 1

N,M = map(int,input().split())
mapping = [list(map(int,input().split())) for _ in range(N)]
nums = []
minV = N*M
visited = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if mapping[i][j]:
            if mapping[i][j] != 6:
                nums.append([i,j,mapping[i][j]])
            elif mapping[i][j] == 6:
                visited[i][j] = 9

n = len(nums)
DFS(n,0,nums,visited)
print(minV)
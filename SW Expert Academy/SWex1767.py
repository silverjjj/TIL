# SWex1767. [SW Test 샘플문제] 프로세서 연결하기

'''
최대한 많은 Core에 전원을 연결하였을 경우, 전선 길이의 합을 구하고자 한다.
단, 여러 방법이 있을 경우, 전선 길이의 합이 최소가 되는 값을 구하라.

7
0 0 1 0 0 0 0
0 0 1 0 0 0 0
0 0 0 0 0 1 0
0 0 0 0 0 0 0
1 1 0 1 0 0 0
0 1 0 0 0 0 0
0 0 0 0 0 0 0
'''
dx = [-1,0,1,0] # 위 오 아래 왼
dy = [0,1,0,-1]


def dfs(k,total):
    global max_Core, min_line
    # print("---------------------------------")
    visited = [[0]*N for _ in range(N)]
    # for a,b in total:
    #     visited[a][b] = 1
    # for row in visited:
    #     print(row)
    if k >= n:
        for a, b in total:
            visited[a][b] = 1
        for row in visited:
            print(row)
        print("----------------------------------------")
        if sum(semi_used) >= max_Core:
            max_Core=sum(semi_used)
            if min_line > len(total):
                min_line = len(total)
            # print("결과값~~~~~~~~~~~~~~~~~~~~~~~~~~~~``")
                # print(max_Core,min_line)
        return
    # print("total : ",total)
    print(semi_used,k)
    if not semi_used[k]:
        semi_used[k] = 1
        x = semi_location[k][0]
        y = semi_location[k][1]
        for l in range(4):
            nx = x + dx[l]
            ny = y + dy[l]
            flag = True
            tmp = []

            if semi[nx][ny] != 1:
                if k == 0:
                    while 0<=nx<N and 0<=ny<N and flag and semi[nx][ny]==0:
                        if [nx,ny] not in total:
                            tmp.append([nx,ny])
                            nx += dx[l]
                            ny += dy[l]
                        else:
                            flag = False
                elif k == 1:
                    while 0<=nx<N and 0<=ny<N and flag and semi[nx][ny]==0:
                        if [nx,ny] not in total:
                            tmp.append([nx,ny])
                            nx += dx[l]
                            ny += dy[l]
                        else:
                            flag = False
                elif k == 2:
                    while 0 <= nx < N and 0 <= ny < N and flag and semi[nx][ny]==0:
                        if [nx, ny] not in total:
                            tmp.append([nx, ny])
                            nx += dx[l]
                            ny += dy[l]
                        else:
                            flag = False
                elif k == 3:
                    while 0<=nx<N and 0<=ny<N and flag and semi[nx][ny]==0:
                        if [nx,ny] not in total:
                            tmp.append([nx,ny])
                            nx += dx[l]
                            ny += dy[l]
                        else:
                            flag = False

                if flag == True:
                    for tp in tmp:
                        total.append(tp)
                    # print("tmp : ",tmp)
                    dfs(k+1, total)
                    # print("도착후", tmp)
                    if len(tmp) != 0:
                        for tp in tmp:
                            total.remove(tp)

    semi_used[k] = 0



N = int(input())
semi = [list(map(int,input().split())) for _ in range(N)]
semi_location=[]
for i in range(1,N-1):
    for j in range(1,N-1):
        if semi[i][j] == 1:
            semi_location.append([i,j])
max_Core = 0
min_line = 987654
n = len(semi_location)
semi_used = [0]*n
done = []

print(semi_location)
dfs(0,total=[])
print(min_line)
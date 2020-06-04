# SWex1767. [SW Test 샘플문제] 프로세서 연결하기

'''
최대한 많은 Core에 전원을 연결하였을 경우, 전선 길이의 합을 구하고자 한다.
단, 여러 방법이 있을 경우, 전선 길이의 합이 최소가 되는 값을 구하라.
1
7
0 0 1 0 0 0 0
0 0 1 0 0 0 0
0 0 0 0 0 1 0
0 0 0 0 0 0 0
1 1 0 1 0 0 0
0 1 0 0 0 0 0
0 0 0 0 0 0 0
'''
# dx = [-1,0,1,0] # 위 오 아래 왼
# dy = [0,1,0,-1]
delta = [(-1,0),(0,1),(1,0),(0,-1)]

# 유효성 검사
def promising(i,j,di,dj):
    # print("유효성 검사",i,j,di,dj)
    while 0<=i<N and 0<=j<N:
        if semi[i][j] == 1:
            # print("유효성검사 실패")
            return False
        i += di
        j += dj
    return True


def dfs(depth,total):
    global max_visited, minV,cnt
    # print(visited)
    # if max_visited == m and sum(visited) < m:
    #     return

    if depth == m:
        # print("도착!!!")
        if sum(visited) >= max_visited:
            max_visited = sum(visited)
            if minV > total:
                minV = total
        # print(max_visited,minV)
        return
    # cnt +=1
    # print(cnt)
    for i in range(len(semi_location)):
        # print(i,semi_location)
        x = semi_location[i][0]
        y = semi_location[i][1]
        # print("x,y = >",x,y)
        for dx,dy in delta:
            # print(x,y,dx,dy)
            # 유효성 검사
            used_semi = []
            # print("유효성 검사 시작전 => ",x,y,dx,dy)
            if visited[i] == 1:
                continue
            if promising(x+dx,y+dy,dx,dy):
                # print("유효성검사 통과")
                tmp_x = x+dx
                tmp_y = y+dy
                # 1로 치환
                while 0 <= tmp_x < N and 0 <= tmp_y < N:
                    if semi[tmp_x][tmp_y] == 1:
                        break
                    used_semi.append([tmp_x, tmp_y])
                    semi[tmp_x][tmp_y] = 1
                    tmp_x += dx
                    tmp_y += dy

                visited[i] = 1
                total += len(used_semi)
                dfs(depth+1,total)
                total -= len(used_semi)
                visited[i] = 0
                for _x,_y in used_semi:
                    semi[_x][_y] = 0
    # return

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    semi = [list(map(int,input().split())) for _ in range(N)]
    semi_location=[]
    for i in range(1,N-1):
        for j in range(1,N-1):
            if semi[i][j] == 1:
                semi_location.append([i,j])
    m = len(semi_location)
    visited = [0]*m
    max_visited = 0
    cnt = 0
    minV = 1234567890
    dfs(0,0)
    print("#{} {}".format(tc,minV))
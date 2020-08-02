# 조합이랑 dfs로 푸는거같음..근데 조합을 모름..

'''
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
'''
def dfs(rm):  # 3개의 벽(1)을 조합으로 넣는것
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    stack = []
    visited = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if rm[i][j] ==2:
                stack.append((i,j))     # 각각의 rm의 바이러스를 찾고 스택에 넣는다.

    while len(stack):
        cx,cy = stack.pop()
        visited[cx][cy] =1
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and rm[nx][ny] == 0:
                rm[nx][ny] = 2
                stack.append((nx,ny))


def comb(arr,idx,cnt): # 조합함수 이거 암기하자.. 내가 부족한부분.
    '''
    마지막 인덱스까지 갔을때 세가지를 모두 선택하지 못했다면 조건 불충족
    '''
    global maxV
    if cnt == 3: # 모든경우의 수를 구했으니, 더이상 진행할필요없음.
        # print(arr)
        # 새로운 보드를 복사하는 과정
        tmpboard = []
        #tmpboard = board.copy() 얕은복사라서 안됨 > 깊은복사해야함
        for b in board:
            # tmpboard.append([l for l in b])
            # tmpboard = [i[:] for i in board]
            tmplist = []
            for e in b:
                tmplist.append(e)
            tmpboard.append(tmplist)

        for i in range(len(arr)):
            if arr[i] == 1:
                r = i // m  # 열
                c = i % m  # 행
                # 벽을 세우기 위한 3개의 좌표
                # print((r,c),end = " ")
                tmpboard[r][c] = 1 # 3개의 벽을 새움
        # ㅂㅏ이러스 퍼뜨리기(dfs로 빈칸에 바이러스 뿌리자)
        # 남아있는 칸의 개수 세기
        # print(tmpboard)
        dfs(tmpboard)
        cnt = 0
        for i in range(n):
            for j in range(m):
                if tmpboard[i][j] == 0:
                    cnt +=1
        if cnt > maxV:
            maxV = cnt
        return
    if idx ==len(arr):  # 세개를 고르지 못하고, 마지막인덱스까지 모두 검사함.
        return
    # 위 두가지 경우에 부합하지 않는다면, 아직 세 위치를 정하지 못한것이다. 다음으로 진행
    # 이번 인덱스 요소를 사용할지 안할지를 결정해서 다음단계로 진행
    # 시간을 줄이기위해 경우의 수를 줄여줍시다.!!

    tmpr = idx//m # 열
    tmpc = idx % m # 행
    if board[tmpr][tmpc] == 0:  # board에서 0인부분에만 가서 >>> 전체 안들리고 시간을 줄일수 있음음
        arr[idx]=1 #idx를 사용했기 때문에 cnt+1
        comb(arr,idx+1,cnt+1)

    arr[idx]=0
    comb(arr,idx+1,cnt)

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
# 조합을 구해서 해당 조합이 의미하는 칸에 벽을 세울건데..
maxV = 0
arr = [0]*(n*m) # 1차원배열을 활용
comb(arr,0,0)
print(maxV)



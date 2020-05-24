# SWex 5653. [모의 SW 역량테스트] 줄기세포배양
'''
K시간동안 번식을 진행함,,

동시에 번식할 경우, 큰수가 번실을 한다.
활성상태때 번식하는거
생명력 수치가 1인경우
초기상태 / 1시간  /2시간/3시간,/4시간,
비활성  / 활성  /비활성 /활성/비활성

생명력 수치가 2인경우
초기상태, 1시간 ,2시간, 3시간, 4시간, 5시간]
비 활 성       /  활 성     / 비 활 성
생명력 수치가 3인경우
초기상태, 1시간 ,2시간, 3시간, 4시간, 5시간
비활성               / 활성               /
생명력 수치 * 2시간 마다 번식을함

번식이 가장 빠른건 생명력수치 1이가진놈인데, 이건 2시간에 상화좌우 1칸씩 늘어남
최대 k 시간이니까, 여유있게 (m+k) *(n+k)정도의 배열이 필요
=> index=시간에 따른 세포의 위치를 만드는 배열 생성
=> 모든 세포 가운대로 이동 => i+k//2 , j+ k // 2
=> 배열을 확장하면서 세포가 존재할경우

1초때 index = 1자리에 있는 자리로 상하좌우 모든 자리에 번식하고 그 자리를 다시 index 1에 append
K = 10초면
1초때 => 세포 1번식
2초때 => 세포1,2 번식
3초때 => 세포1,2,3 번식

입력
5 5 19
3 2 0 3 0
0 3 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 2
'''
dx = [-1,0,1,0]
dy = [0,1,0,-1]
N,M,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
cells = [[0] *(M+K) for _ in range(N+K)]
active = [[-1] *(M+K) for _ in range(N+K)]
# cell_list = [[] for _ in range(11)]
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0:
            cells[i+K//2][j+K//2] = arr[i][j]
# k = K // 2
time = 0
while time < K:
    time +=1
    cell_add = []
    for x in range(N+K-1):
        for y in range(M+K-1):
            if cells[x][y] != 0:
                if 0 <=(time % (cells[x][y]*2)) < time:   #비활성화 시작
                    tmp = active[x][y]
                    active[x][y] = tmp - 1
                    continue
                if time % cells[x][y] == 0:
                    cell_add.append([x, y, cells[x][y]])
                    active[x][y] = cells[x][y]
                #
                # if time % 2 == 1 and cells[x][y] == 1:
                #     cell_add.append([x,y,cells[x][y]])
                #     continue
                # if time >= 2 and cells[x][y] > 1:
                #     # print(time,cells[x][y])
                #     if time % cells[x][y] == 0:
                #         cell_add.append([x,y,cells[x][y]])

    cell_add.sort(key=lambda x:x[2], reverse=True)
    print("------------------------------------------------")
    print(cell_add, len(cell_add))
    for cell in cell_add:
        x = cell[0]
        y = cell[1]
        v = cell[2]
        active[x][y] = 0
        for l in range(4):
            nx = x + dx[l]
            ny = y + dy[l]
            # 비어있어야 전파
            if cells[nx][ny] == 0:
                cells[nx][ny] = v
                # 해당 위치 활성화표시
                # active[nx][ny] = 1
    # print(time)
    for row1 in cells:
        print(row1)
    # 활성상태 만드는 로직
    # cell_add = []
    # for x in range(N+K-1):
    #     for y in range(M+K-1):
    #         if cells[x][y]:
    #             if time % 2 == 1 and cells[x][y] == 1:
    #                 cell_add.append([x,y,cells[x][y]])
    #                 continue
    #             if time >= 2 and cells[x][y] > 1:
    #                 # print(time,cells[x][y])
    #                 if time % cells[x][y] == 0:
    #                     cell_add.append([x,y,cells[x][y]])

print("------------------------------------------------")
result = 0
cnt = 0
for i in range(N + K - 1):
    for j in range(M + K - 1):
        if active[i][j] !=0:
            cnt +=1
print(cnt)

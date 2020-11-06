# SWex2382. [모의 SW 역량테스트] 미생물 격리
dx = [0, -1, 1, 0, 0]  # x 상 하 좌 우
dy = [0, 0, 0, -1, 1]

T = int(input())
for tc in range(1,T+1):
    n,m,k = map(int,input().split())
    cell = dict()
    for _ in range(k):
        x,y,cnt,l = list(map(int,input().split()))
        # 위치 : 갯수,이동방향  딕셔너리형태로 생성
        cell[(x,y)] = [[cnt,l]]
    while m > 0:
        m-=1
        cell_list = []
        new_cell = dict()
        for key,value in cell.items():
            x,y = key
            cnt,l = value[0][0],value[0][1]
            # 새로운 위치
            nx,ny = x + dx[l], y + dy[l]
            # 가장자리 =>미생물은 // 2, 여기에 들어가면 방향은 반대
            if nx == 0 or ny == 0 or nx == n-1 or ny == n-1:
                cnt = cnt // 2
                if l % 2 == 0: l -= 1
                else: l += 1
            if cnt == 0:
                continue
            if new_cell.get((nx,ny)):
                if [nx,ny] not in cell_list:
                    cell_list.append([nx,ny])
                new_cell[(nx,ny)].append([cnt,l])
            else:
                new_cell[(nx,ny)] = [[cnt,l]]
        for x,y in cell_list:
            v = new_cell[(x,y)]
            # print(v)
            sum = 0
            maxV = 0
            maxL = 0
            for i,j in v:
                # print(i,j)
                sum += i
                if i > maxV:
                    maxV = i
                    maxL = j
            new_cell[(x,y)] = [[sum,maxL]]
        cell = new_cell
    result = 0
    for q in list(cell.values()):
        result += q[0][0]
    print("#{} {}".format(tc,result))


'''
기둥은 바닥위 or 보의 한쪽끝 or 다른 기둥 위
보는 한쪽보가 기둥 위 or 양쪽이 보랑 연결

x,y,a,b
x,y : 좌표
a : 0 기둥, 1 보
b : 0 삭제, 1 설치
'''
def solution(n, build_frame):
    arr = []
    gidung = [[0]*(n+1) for _ in range(n+1)]
    bo = [[0]*(n+1) for _ in range(n+1)]
    build = [[0]*(n+1) for _ in range(n+1)]
    for x,y,a,b in build_frame:
        if b == 1: # 설치
            if a == 0: # 기둥
                if (y == 0) or bo[x][y] == 1 or gidung[x][y] == 1:
                    # build[x][y] += 2; build[x][y+1] += 2
                    gidung[x][y] = 1; gidung[x][y+1] = 1
                    arr.append([x,y,a])
            elif a == 1: # 보
                if (gidung[x+1][y] == 1 or gidung[x][y] == 1) or (bo[x+1][y] >= 1 and bo[x][y] == 1):
                    bo[x + 1][y] = 1; bo[x][y] = 1
                    arr.append([x, y, a])
        # else: # 해제
        #     if a == 0:  # 기둥
        #         if build[x][y+1] >= 2 and build[x][y+1] >= 2:
        #             build[x][y + 1] -= 2;  build[x][y] -= 2
        #             # gidung[x][y] = 0
        #             # gidung[x][y + 1] = 0
        #             arr.remove([x,y,a])
        #             # arr.remove([x, y+1, a])
        #     elif a == 1: # 보
        #         if build[x + 1][y] >= 3 and  build[x][y] >= 3:
        #             build[x + 1][y] -= 1; build[x][y] -= 1
        #             # bo[x+1][y] = 0
        #             # bo[x][y] = 0
        #             arr.remove([x, y, a])
        #             # arr.remove([x + 1, y, a])
    print("==================================")
    for row in build:
        print(row)
    arr.sort()
    print(arr)
    # print("==================================")
    # res = []
    # for i in range(n+1):
    #     for j in range(n+1):
    #         if 0 <= bo[i][j] < n and 0 <= bo[i+1][j] < n:
    #             if bo[i][j]:
    #                 res.append([i,j,0])
    #                 continue
    #         if 0<= gidung[i][j+1] < n and 0<= gidung[i][j+1]< n:
    #             if
    #     print(row)
    # print("==================================")
    # for row in bo:
    #     print(row)
    # arr.sort()
    # print(arr)
    return arr

n = 5
# build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
solution(n, build_frame)
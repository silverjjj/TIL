'''
약품이 칠해진셀(가장 바깥셀)에 도착하면 미생물수//2를 해준뒤, 방향은 반대로바뀜
미생물끼리 만날경우 군집의 미생물수를 합해준다. 이때 이동방향은
미생물수가 많은군집의방향
n : 정사각형의 변
m : 시간
k는 미생물의 갯수
a,b,c,d
세로위치,가로위치,미생물수,이동방향(1,2,3,4 상하좌우)
'''
'''
알고리즘: 
일단 조건에 맞게 표를 만들자
조건:
1초씩 흐르면서 이동을 시켜줘
이때, 바깥셀 => 방향 반대, 미생물//2
이때, 
'''
import copy
dx = [0,-1,1,0,0]   # x 상 하 좌 우
dy = [0,0,0,-1,1]
n,m,kk = map(int,input().split())

arr = []
for j in range(kk):
    bug = list(map(int,input().split()))
    arr.append(bug)
print(arr)
edge = []
# 가장자리
for i in range(n):
    edge.append([0,i])
    edge.append([n-1,i])
    edge.append([i,0])
    edge.append([i,n-1])
# print(edge)
# 시간
# visited = [[0] * n for _ in range(n)]
for j in range(m):
    visited = [[0] * n for _ in range(n)]
    for i in range(len(arr)):
        x = arr[i][0]
        y = arr[i][1]
        cnt = arr[i][2]
        k = arr[i][3]
        # 새로운 위치 위치와 조건을 만들자
        nx = x + dx[k]
        ny = y + dy[k]
        # visited[nx][ny] = [x,y,cnt,k]
        if [nx,ny] in edge:
            cnt = cnt // 2
            # 짝수
            if k % 2 == 0:
                k -=1
            else:# 홀수
                k+=1
        if visited[nx][ny] !=0:
            x2,y2,cnt2,k2 = visited[nx][ny]
            if cnt2 > cnt:
                cnt2+=cnt
                visited[nx][ny] = [x2,y2,cnt2,k2]
            else:
                cnt+=cnt2
                visited[nx][ny] = [nx, ny, cnt, k]
        else:
            visited[nx][ny] = [nx, ny, cnt, k]


        arr = [[0] * n for _ in range(n)]
        for row in visited:
            for j in range(n):
                for i in range(n):
                    if type(row[i]) ==list:
                        arr[i][j] = row[i]
        for row in arr:
            print(row)


'''
7 2 9   
1 1 7 1 
2 1 7 1
5 1 5 4
3 2 8 4 
4 3 14 1
3 4 3 3 
1 5 8 2 
3 5 100 1
5 5 1 1
'''
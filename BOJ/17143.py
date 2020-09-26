'''
1. 상호 번호별 정보를 담은 딕셔너리
2. 2차원 배열에 상어 번호 할당
3. 잡는다
4. 이동 : 딕셔너리 한개씩 빼주면서 갱신
4-1. 이동할때 양쪽 방향 전환할때 주의
5. 2차원 배열에 재배치 (상어 크기 비교하면서)
'''
dx = [0,-1,1,0,0] # 위 아래 오른 왼
dy = [0,0,0,1,-1]
change = [0,2,1,4,3]

def move(shark):
    for key, val in shark.items():
        x = val[0]
        y = val[1]
        s = val[2]
        d = val[3]
        z = val[4]
        tmp = s
        if d <= 2:
            while tmp > 0:
                tmp -= 1
                if 1 < x < X or (x == 1 and d == 2) or (x == X and d == 1):
                    x += dx[d]
                elif x == 1 or x == X:
                    d = change[d]
                    x += dx[d]
        else:
            while tmp > 0:
                tmp -= 1
                if 1 < y < Y or (y == 1 and d == 3) or (y == Y and d == 4):
                    y += dy[d]
                elif y == 1 or y == Y:
                    d = change[d]
                    y += dy[d]
        shark[key] = [x,y,s,d,z]
    return shark


X,Y,M = map(int,input().split())
shark = {}
# r,c,s,d,z
visited = [[0]*(Y+1) for _ in range(X+1)]
for i in range(1,M+1):
    arr = list(map(int,input().split()))
    shark[i] = arr
for key, val in shark.items():
    visited[val[0]][val[1]] = key
num = 1
res = 0
while num <= Y:
    # 상어 잡는다.
    for i in range(1,X+1):
        if visited[i][num]:
            rm = visited[i][num]
            res += shark[rm][4]
            visited[shark[rm][0]][shark[rm][1]] = 0
            del shark[rm]
            break

    for arr in shark.values():
        visited[arr[0]][arr[1]] = 0
    # 상어 이동
    shark = move(shark)
    after_rm = []
    for key, val in shark.items():
        if not visited[val[0]][val[1]]:
            visited[val[0]][val[1]] = key
        else:
            number = visited[val[0]][val[1]]
            if shark[number][4] < shark[key][4]:
                after_rm.append(number)
                visited[val[0]][val[1]] = key
            else:
                after_rm.append(key)
    if len(after_rm) > 0:
        for l in after_rm:
            del shark[l]
    num += 1
print(res)
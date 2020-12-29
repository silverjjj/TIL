'''
BOJ 3055
'''
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    global cnt

    while animal:
        cnt += 1
        A = len(animal)
        for _ in range(A):
            x,y = animal.pop(0)
            if arr[x][y] != 'S':
                continue
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < R and 0 <= ny <C:
                    if arr[nx][ny] == '.':
                        animal.append([nx,ny])
                        arr[nx][ny] = 'S'
                    elif arr[nx][ny] == "D":
                        return True

        W = len(water)
        for _ in range(W):
            i,j = water.pop(0)  # 만약에 물이 없다면?
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < R and 0 <= nj <C:
                    if arr[ni][nj] != 'X' and arr[ni][nj] != 'D' and arr[ni][nj] != '*':
                        arr[ni][nj] = '*'
                        water.append([ni,nj])
    return False

R,C =map(int,input().split())
arr = []
animal = []
water = []
for i in range(R):
    tmp = list(map(str,input()))
    for j in range(C):
        if tmp[j] == '*':
            water.append([i,j])
        elif tmp[j] == 'S':
            animal.append([i,j])
    arr.append(tmp[:])
cnt = 0
if bfs():
    print(cnt)
else:
    print('KAKTUS')
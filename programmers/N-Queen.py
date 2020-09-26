
def horizontal(n,x,arr):
    for j in range(n):
        arr.append([x,j])
def vertical(n,y,arr):
    for i in range(n):
        arr.append([i,y])
def diagonal(n,x,y,arr):
    cnt = 1
    while True:
        nx = x - cnt
        ny = y - cnt
        if 0<= nx <n and 0<=ny<n:
            arr.append([nx,ny])
        else:
            break
        cnt += 1
    cnt = 1
    while True:
        nx = x - cnt
        ny = y + cnt
        if 0<= nx <n and 0<=ny<n:
            arr.append([nx,ny])
        else:
            break
        cnt += 1
    cnt = 1
    while True:
        nx = x + cnt
        ny = y - cnt
        if 0<= nx <n and 0<=ny<n:
            arr.append([nx,ny])
        else:
            break
        cnt += 1
    cnt = 1
    while True:
        nx = x + cnt
        ny = y + cnt
        if 0<= nx <n and 0<=ny<n:
            arr.append([nx,ny])
        else:
            break
        cnt += 1

def find(n,x,visited):
    print("====================================")
    print(x,"층")
    for row in visited:
        print(row)
    if n == x:
        print("도착!!")
        return
    for y in range(n):
        if not visited[x][y]:
            print(x,y)
            arr = []
            horizontal(n,x,arr)
            vertical(n,y,arr)
            diagonal(n,x,y,arr)
            for i,j, in arr:
                visited[i][j] = 1
            # visited[x][y] -= 1
            find(n, x+1, visited)
            for i,j, in arr:
                visited[i][j] = 0
    return
def solution(n):
    answer = 0
    visited = [[0]*n for _ in range(n)]
    find(n,0,visited)
    return answer
n = 4
solution(n)
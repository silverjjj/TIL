'''
문이 0개일때 고려해야함

'''
import sys, copy
from collections import deque

input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def BFS():
    tmp_prison = copy.deepcopy(prison)
    dq = deque([])
    res = 0
    print(person)
    visited = [[[0]*len(person) for _ in range(M)] for _ in range(N)]
    weight = [[[0]*len(person) for _ in range(M)] for _ in range(N)]
    cnt = 0
    for sx,sy in person:
        dq.append([sx, sy, cnt])
        cnt += 1
    flag = False
    print(dq)
    while dq:
        x, y, num = dq.popleft()
        visited[x][y][num] = 1
        cur = weight[x][y][num]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny][num] and (tmp_prison[nx][ny] == "." or tmp_prison[nx][ny] == "$" or tmp_prison[nx][ny] == "#"):

                visited[nx][ny][num] = 1
                dq.append([nx, ny, num])
                if tmp_prison[nx][ny] == "#":
                    # tmp_prison[nx][ny] = "."
                    weight[nx][ny][num] += (cur + 1)
                else:
                    weight[nx][ny][num] += cur
                if nx == 0 or nx == N-1 or ny == 0 or ny == M-1:
                    print("탈출~~~~~~~`")

                # dq.append([nx, ny, num])

    #     if flag:
    #         res += 1
    print("==============")
    for r in visited:
        print(r)
    print("=======================")
    for r in weight:
        print(r)
    # if res == len(person):
    #     print("탈출!!!!!!!!!!!!!!!!!")
        # return True
N,M = map(int,input().split())
prison = []
door = []
person = []
for i in range(N):
    arr = list(map(str, input().strip()))
    prison.append(arr[:])
    for j in range(M):
        if arr[j] == "#":
            door.append([i,j])
        elif arr[j] == "$":
            person.append([i,j])

BFS()

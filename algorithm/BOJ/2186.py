'''
8퍼 시간초과

'''
from collections import deque
import sys
input = sys.stdin.readline

def BFS(st):
    dq = deque([st])
    cnt = 1
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[st[0]][st[1]] += 1
    while dq and len(chars) > cnt:
        L = len(dq)
        # print(dq)
        for _ in range(L):
            x,y = dq.popleft()
            for nx,ny in dict.get(chars[cnt]):
                if not visited[nx][ny]:
                    if (abs(x - nx) + abs(y - ny)) <= K:
                        visited[nx][ny] = 1
                        dq.append([nx,ny])
                else:
                    if (abs(x - nx) + abs(y - ny)) <= K:
                        visited[nx][ny] = 1 + visited[x][y]
        cnt += 1
    # for r in visited:
    #     print(r)
    # print(dq)
    tmp = 0
    for i,j in dq:
        tmp += visited[i][j]
    return tmp
N,M,K = map(int,input().split())
room = [list(map(str,input())) for _ in range(N)]
chars = str(input().rstrip())
dict = {}
for char in chars:
    dict[char] = []
for i in range(M):
    for j in range(N):
        if dict.get(room[i][j]) != None:
            dict[room[i][j]].append([i,j])
res = 0
for st in dict.get(chars[0]):
    res += BFS(st)
print(res)

'''


4 4 3
KAKT
XEAS
YREU
ZBBR
BREAK

'''
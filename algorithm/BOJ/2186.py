'''
8퍼 시간초과
딕셔너리를 사용하면 문자판에 있는 모든 K의 문자를 담으니까 메모리초과가 발생
메모이제이션 + dfs
'''
from collections import deque
import sys
input = sys.stdin.readline

d = [(0,1),(0,-1),(1,0),(-1,0)]
def BFS(x, y, idx):
    if idx == len(char):
        return 1
    if visited[x][y][idx] != -1:
        return visited[x][y][idx]

    visited[x][y][idx] = 0
    for add in range(1,K+1):
        for dx,dy in d:
            nx = x + (dx*add)
            ny = y + (dy*add)
            if 0<=nx<N and 0<=ny<M:
                if room[nx][ny] == char[idx]:
                    visited[x][y][idx] += BFS(nx, ny, idx+1)

    return visited[x][y][idx]


N,M,K = map(int,input().split())
room = [list(map(str,input())) for _ in range(N)]
char = str(input().rstrip())
chars = []
for i in range(N):
    for j in range(M):
        if room[i][j] == char[0]:
            chars.append([i,j])

visited = [[[-1]*len(char) for _ in range(M)] for _ in range(N)]  # 3차원 리스트로 위치 and 방문표시
ans = 0
for x,y in chars:
    ans += BFS(x,y,1)
print(ans)

'''


4 4 2
KAKT
XEAE
YREU
ZBBR
BREAK

'''
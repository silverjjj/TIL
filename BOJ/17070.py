'''
DFS로 풀수 있는 문제지만, 시간초과가 발생
DP로 반복규칙을 파악한뒤 다시 구했음
'''
import sys
# from collections import deque
input = sys.stdin.readline

# dx = [0,1,1]   # index 0~2은 각각 가로, 세로 대각선방향
# dy = [1,0,1]
# directions = [[0,2],[1,2],[0,1,2]]
#
# def BFS():
#     for _ in range(len(dq)):
#         x, y, d = dq.popleft()
#         for k in directions[d]:
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0<=nx<N and 0<=ny<N and not room[nx][ny]:
#                 if k == 2 and (room[x][y+1] or room[x+1][y]):
#                     continue
#                 if nx ==N-1 and ny == N-1:
#                     visited[nx][ny] += 1
#                     continue
#                 dq.append([nx,ny,k])
#                 visited[nx][ny] += 1
#
# def BOJ17070():
#     global room,dq,visited,N
#     N = int(input())
#     room = [list(map(int,input().split())) for _ in range(N)]
#     visited = [[0 for _ in range(N)] for _ in range(N)]
#     visited[0][0] = visited[0][1] = 1
#     dq = deque([])
#     dq.append([0,1,0])
#     while True:
#         BFS()
#         if len(dq) == 0:
#             break
#
# BOJ17070()



N = int(input())
room = [list(map(int,input().split())) for _ in range(N)]
dp = [[[0]*3 for _ in range(N)] for _ in range(N)]

# 0 : ㅡ, 1:|, 2: /
dp[0][1][0] = 1
for j in range(2,N):
    if not room[0][j]:
        dp[0][j][0] = dp[0][j-1][0]

for x in range(1,N):
    for y in range(1,N):
        if not room[x][y] and not room[x-1][y] and not room[x][y-1]:
            dp[x][y][2] = dp[x-1][y-1][0] + dp[x-1][y-1][1] + dp[x-1][y-1][2]
        if not room[x][y]:
            dp[x][y][0] = dp[x][y-1][0] + dp[x][y-1][2]
            dp[x][y][1] = dp[x-1][y][1] + dp[x-1][y][2]

print(sum(dp[N-1][N-1][i] for i in range(3)))
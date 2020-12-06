# 17144번 미세먼지 안녕!
'''
1. 청소기의 x위치를 찾는다.
2.
'''
import sys
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]
d = ((0,1),(1,0),(0,-1),(-1,0))

# def Diffusion(room):
#     visited = [[0 for _ in range(M)] for _ in range(N)]
#     for i in range(N):
#         for j in range(M):
#             if (not room[i][j] or mapping[i][j] == -1): # 미세먼지가 없거나 공기청정기
#                 continue
#             tmp = []
#             cnt2 = 0
#             for k in range(4):
#                 nx = i + dx[k]
#                 ny = j + dy[k]
#                 if 0<=nx<N and 0<=ny<M and mapping[nx][ny] == 0:
#                     tmp.append([nx,ny,room[i][j]//5])
#                     cnt2 += 1
#             tmp.append([i,j,(room[i][j] - (room[i][j]//5)*cnt2)])
#             for x,y,w in tmp:
#                 visited[x][y] += w
#
#     return visited[:]


def Diffusion():
    dusts = {}
    for i in range(N):
        for j in range(M):
            if mapping[i][j] == 0:
                dusts[str(i) + str(j)] = 0
                continue
            elif mapping[i][j] == -1:
                dusts[str(i) + str(j)] = -1
                continue

            dusts[str(i)+str(j)] = mapping[i][j]
            next = mapping[i][j] // 5
            cnt = 0
            for dx,dy in d:
                nx = i + dx
                ny = j + dy
                if 0<=nx<N and 0<=ny<M and mapping[nx][ny] > 0:
                    cnt += 1
                    if dusts.get(str(nx)+str(ny)) is None:
                        dusts[str(nx)+str(ny)] = next
                    else:
                        dusts[str(nx)+str(ny)] += next
            dusts[str(i)+str(j)] -= (next * cnt)
    print(dusts)
N,M,T = map(int,input().split())
mapping = []    # 집
cleaner = []    # 청소기 위치
for i in range(N):
    arr = list(map(int,input().split()))
    if -1 in arr:
        cleaner.append(i)
    mapping.append(arr)
print(cleaner)

for _ in range(T):
    Diffusion()
for r in mapping:
    print(r)


# while cnt <= T:
#     cnt += 1
#     Diffusion(room)
#     aircon()
#     for row in room:
#         print(row)
#     # print("=======================")
#     # for row in mapping:
#     #     print(row)
#
# # print(cleaner)

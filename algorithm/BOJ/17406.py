'''
BOJ 17406

회전 알고리즘
순열 알고리즘
'''
import copy, sys
input = sys.stdin.readline

d = ((0,1),(1,0),(0,-1),(-1,0))
def find(x,y):
    pre = arr[x][y]
    for dx,dy in d:
        while st_n<= x+dx < n and st_m<= y+dy < m and not visited[x+dx][y+dy]:
            visited[x][y] = 1
            x = x + dx
            y = y + dy
            cur = arr[x][y]
            arr[x][y] = pre
            pre = cur
    arr[x+dx][y+dy] = pre

def perm(k):
    if l == k:
        plist.append(p[:])
        return
    else:
        for i in range(l):
            if not used[i]:
                used[i] = 1
                p[k] = tmp[i]
                perm(k+1)
                used[i] = 0

N, M, K = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(N)]
RCS = [list(map(int,input().split())) for _ in range(K)]

tmp = [i for i in range(K)]
l = len(tmp)
p = [0]*l
used = [0]*l
plist = []
perm(0)
minV = float('inf')

for lst in plist:
    arr = copy.deepcopy(room)
    for i in lst:
        r,c,s = RCS[i]
        st_n = r-s-1
        st_m = c-s-1
        n = r+s
        m = c+s
        visited = [[0] * M for _ in range(N)]
        for add in range((m-st_m)//2):
            find(st_n+add,st_m+add)
    for r in arr:
        minV = min(minV, sum(r))
    if minV == 0:
        break

print(minV)
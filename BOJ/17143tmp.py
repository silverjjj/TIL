
X,Y,M = map(int,input().split())
shark = []
# r,c,s,d,z
visited = [[0]*Y for _ in range(X)]
for m in range(M):
    x, y, s, d, z = list(map(int,input().split()))\
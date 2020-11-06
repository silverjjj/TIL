N, K = map(int,input().split())
mapping = [[0 for _ in range(N+1)] for _ in range(K)]
mapping[0][:] = [1 for _ in range(N+1)]
maxV = 1000000000
for k in range(K):
    mapping[k][0] = 1
for j in range(1,N+1):
    for i in range(1,K):
        mapping[i][j] = (mapping[i-1][j] + mapping[i][j-1]) % maxV
print(mapping[-1][-1])
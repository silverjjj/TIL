N,K= map(int,input().split(' '))
data = []
result = 0
for i in range(N):
    for j in range(N):
        data[i][j]
        cnt = 0
        if data[i][j] ==1:
            cnt +=1
            if cnt ==K and j == N-1:
                result +=1
            else
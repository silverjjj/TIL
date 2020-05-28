def find():
    home = 0
    for i in range(N):
        for j in range(N):
            distance = [0]*(2*N)
            for x,y in house:
                # 모든 점을 기준으로 집이 있는 거리의 위치반경(index)에 +1을 해준다
                distance[abs(i-x)+ abs(j-y)+1]+=1
            # print(distance)
            for k in range(1,N+2):
                distance[k] += distance[k-1]
                res = distance[k]
                if res*M >= k*k+(k-1)*(k-1):
                    home = max(home,res)
    return home

N,M = map(int,input().split())
rm = [list(map(int,input().split())) for _ in range(N)]
house = []

for i in range(N):
    for j in range(N):
        if rm[i][j]:
            house.append((i,j))
print(find())
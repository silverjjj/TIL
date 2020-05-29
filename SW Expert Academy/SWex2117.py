# SWex 2117. [모의 SW 역량테스트] 홈 방범 서비스
def find():
    maxV = 0
    for i in range(N):
        for j in range(N):
            distance = [0]*(2*N)
            # 모든 0,0 ~ N-1,N-1까지 모든점들과 집들 사이의 거리를 구한뒤
            # 해당 idx(여기서 idx는 k에 해당함)에 갯수를 할당
            for x,y in house:
                # 모든 점을 기준으로 집이 있는 거리의 위치반경(index)에 +1을 해준다
                distance[abs(i-x)+ abs(j-y)+1]+=1
            # 한점의 위치와 집들 사이의 거리를 모두 구한 distance배열에서
            # k=1 ~ k=N+1까지의 누적합을 위한 과정
            for k in range(1,N+2):
                distance[k] += distance[k-1]
                res = distance[k]
                # 각각의 k 값마다 적자가 나지않는 조건
                # 해당 조건에 맞아야 서비스를 진행할수 있다.
                if res*M >= k*k+(k-1)*(k-1):
                    if res > maxV:
                        maxV = res

    return maxV

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    rm = [list(map(int,input().split())) for _ in range(N)]
    house = []
    # 집의 모든 위치를 찾아서 house에 push
    for i in range(N):
        for j in range(N):
            if rm[i][j]:
                house.append((i,j))
    print("#{} {}".format(tc,find()))
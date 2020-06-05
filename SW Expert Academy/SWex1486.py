# SWex1486. 장훈이의 높은 선반
def find(k,N,res):
    global minV,cnt
    if res == S:
        minV = res
        return
    if res > S:
        # print(visited)
        if minV > res:
            minV = res
        return
    if k >= N:
        cnt +=1
        # print(visited,cnt)
        return
    # print(visited,k)
    if not visited[k]:
        visited[k] = 1
        find(k+1, N, res+arr[k])
        visited[k] = 0
        find(k+1, N, res)

T = int(input())
for tc in range(1,T+1):
    N, S =map(int,input().split())
    arr = list(map(int,input().split()))
    minV = 9876543
    visited = [0]*N
    cnt = 0
    find(0,N,0)
    print("#{} {}".format(tc,minV-S))
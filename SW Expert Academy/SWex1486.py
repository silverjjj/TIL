# SWex1486. 장훈이의 높은 선반

def find(k,N,res):
    global minV
    if k > N:
        return
    if res >= sum:
        print(sum)
        if res == sum:
            return
        if minV > res:
            minV = res
    else:
        visited[k] = 1
        find(k+1,N, res+arr[k])
        print(k)
        visited[k] = 0
        find(k + 1, N, res)

N, S =map(int,input().split())
arr = list(map(int,input().split()))
minV = 9876543
sum = sum(arr)
print(sum)
visited = [0]*N
find(0,N,0)
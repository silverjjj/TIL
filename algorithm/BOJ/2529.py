def dfs(nums, depth):
    global visited,maxV,minV
    if depth == N:
        num = "".join([str(i) for i in nums])
        if int(num) > int(maxV):
            maxV = num
        if int(num) < int(minV):
            minV = num
        return

    for j in range(10):
        if visited[j]:
           continue

        if arr[depth] == "<" and nums[-1] < j:
            visited[j] = 1
            dfs(nums+[j], depth+1)
            visited[j] = 0

        elif arr[depth] == ">" and nums[-1] > j:
            visited[j] = 1
            dfs(nums+[j], depth+1)
            visited[j] = 0

N = int(input())
arr = list(map(str,input().split()))
maxV = 0
minV = 10000000000
for i in range(10):
    visited = [0]*10
    visited[i] = 1
    dfs([i],0)
print(maxV)
print(minV)

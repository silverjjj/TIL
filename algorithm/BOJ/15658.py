def dfs(idx,res):
    global maxV,minV
    if idx == N:
        maxV = max(res, maxV)
        minV = min(res, minV)
        return
    for k in range(4):
        if arr[k] > 0:
            arr[k] -= 1
            if k == 0:
                dfs(idx + 1,res + nums[idx])
            elif k == 1:
                dfs(idx + 1,res - nums[idx])
            elif k == 2:
                dfs(idx + 1, res * nums[idx])
            elif k == 3:
                dfs(idx + 1, int(res / nums[idx]))
            arr[k] +=1
N = int(input())
nums = list(map(int,input().split()))
arr = list(map(int,input().split()))
maxV = -1000000000
minV = 1000000000
dfs(1,nums[0])
print(maxV)
print(minV)
# 14888_연산자끼워넣기
def dfs(k,result):
    global minV, maxV
    if k == n-1:
        if result > maxV:
            maxV = result
        if minV > result:
            minV = result
        return
    for i in range(4):
        if sign[i] > 0:
            sign[i] -=1
            if i == 0:
                dfs(k + 1, result + arr[k + 1])
            elif i == 1:
                dfs(k + 1, result - arr[k + 1])
            elif i == 2:
                dfs(k + 1, result * arr[k + 1])
            elif i == 3:
                dfs(k + 1, int(result / arr[k + 1]))
            sign[i] += 1

N = int(input())
arr = list(map(int,input().split()))
sign = list(map(int,input().split()))
n = len(arr)
maxV = -100000000
minV = 100000000
dfs(0,arr[0])
print(maxV)
print(minV)
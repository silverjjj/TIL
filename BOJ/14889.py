
def Combination(n,r, maps, arr, tr, res):
    if r == 0:
        res.append(tr[:])
        return
    elif n < r:
        return
    else:
        tr[r-1] = arr[n-1]
        Combination(n-1,r-1, maps, arr, tr, res)
        Combination(n-1,r, maps, arr, tr, res)

def Calculation(res,maps,r):
    minV = 123456789
    sum_res = []
    for nums in res:
        sum = 0
        for i in range(r - 1):
            for add in range(1, r - i):
                x = nums[i]
                y = nums[i + add]
                sum += (maps[x][y] + maps[y][x])
        sum_res.append(sum)
    L = len(sum_res)
    for k in range(L // 2):
        stan = abs(sum_res[k] - sum_res[L - k - 1])
        if minV > stan:
            minV = stan
    return minV
def BOJ14889():
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]
    arr = [i for i in range(n)]
    r = n // 2
    tr = [0] * r
    res = []
    Combination(n, r, maps, arr, tr, res)

    minV = Calculation(res,maps,r)
    print(minV)

BOJ14889()
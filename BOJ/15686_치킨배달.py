
def calculation(tr,homes):
    res = 0
    for home in homes:
        stan = []
        for chicken in tr:
            stan.append(abs(home[0]-chicken[0]) + abs(home[1]-chicken[1]))
        res += min(stan)
        if res > minV:
            return res
    return res

def comb(n,r):
    global minV
    if r == 0:
        res = calculation(tr,homes)
        if minV > res:
            minV = res
    elif n < r:
        return
    else:
        tr[r-1] = chickens[n-1]
        comb(n-1, r-1)
        comb(n-1, r)



n, m = map(int, input().split())
homes = []
chickens = []
minV = 12345678
for i in range(n):
    nums = list(map(int, input().split()))
    for j in range(n):
        if nums[j] == 1:
            homes.append([i, j])
        elif nums[j] == 2:
            chickens.append([i, j])
l = len(chickens)
tr = [0] * m
comb(l, m)
print(minV)
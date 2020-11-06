def find(i, j):
    num = nums[i][j]
    while True:
        if i == 0:
            return j
        for k in range(3):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 < ni <= 100 and 100 <= nj <0:
                continue
            if nums[ni][nj] == 0:
                continue
            if visited[ni][nj] == 1:
                continue
            i = ni
            j = nj
            visited[ni][nj] = 1
            num = nums[ni][nj]
for tc in range(1, 11):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(100)]
    visited = [[0 for x in range(100)] for y in range(100)]
    di = [0, 0, -1]
    dj = [1, -1, 0]
    for i in range(100):
        if nums[99][i] == 2:
            f = find(99,i)

    print("#{} {}".format(tc, f))
def comb(n,r, tmp):
    if r == 0:
        tr_list.append(tr[:])
    elif n < r:
        return
    else:
        tr[r-1] = tmp[n-1]
        comb(n-1, r-1, tmp)
        comb(n-1, r, tmp)

T = int(input())
for tc in range(1,T+1):
    mapping = []
    foods = []
    homes = []
    tr_list = []
    N = int(input())
    for i in range(N):
        arr = list(map(int,input().split()))
        mapping.append(arr[:])
        for j in range(N):
            if arr[j] == 1:
                homes.append([i,j])
            elif arr[j] > 1:
                foods.append([i,j])
    for r in range(1,len(foods)+1):
        tr = [0]*r
        tmp = [i for i in range(len(foods)+1)]
        comb(len(foods), r, tmp)

    minV = float('inf')
    for lst in tr_list:
        res = 0
        for num in lst:
            res += mapping[foods[num][0]][foods[num][1]]
        for x, y in homes:      # 각각의 사람마다 가장 가까운 가게를 찾는다
            tmp = []
            for num in lst:         # lst는 가게번호 모음집
                f_x = foods[num][0]
                f_y = foods[num][1]
                tmp.append(abs(x-f_x) + abs(y-f_y))
            tmp.sort()
            res += tmp[0]
            if res > minV:
                break
        if minV > res:
            minV = res
    print("#{} {}".format(tc, minV))

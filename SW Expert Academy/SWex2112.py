# SWex2112. [모의 SW 역량테스트] 보호 필름

# 유효성 검사
def checked(film, arr_cnt):
    global result
    flag = True
    for j in range(W):
        cnt = 0
        for i in range(D - 1):
            if film[i][j] == film[i + 1][j]:
                cnt += 1
            else:
                cnt = 0
            if cnt == K - 1:
                break
            if i == D - 2:
                flag = False
        if flag == False:
            break
    if flag:
        result = arr_cnt
        return

# 0 or 1로 바꿔주기
def find(tr):
    tmp = []
    for t in tr:
        tmp_zero = [0 for _ in range(W)]
        tmp.append(film[t][:])
        tmp_zero, film[t][:] = film[t][:], tmp_zero
        if checked(film, len(tr)):
            return result
    for t in tr:
        tmp_one = [1 for _ in range(W)]
        tmp_one, film[t][:] = film[t][:], tmp_one
        if checked(film, len(tr)):
            return result
    for t in tr:
        tmp_arr = tmp.pop(0)
        film[t][:] = tmp_arr


# 조합생성
def comb(n, r):
    if r == 0:
        if find(tr):
            return result
    elif n < r:
        return
    else:
        tr[r - 1] = arr[n - 1]
        comb(n - 1, r - 1)
        comb(n - 1, r)


T = int(input())
for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    arr = [i for i in range(D)]
    result = -1
    checked(film, 0)
    if result == -1:
        for k in range(1, K):
            tr = [0] * k
            visited = [0] * k
            p = [0] * k
            comb(D, k)
            if result != -1:
                break
    if result == -1:
        result = K
    print("#{} {}".format(tc, result))
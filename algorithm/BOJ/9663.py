def N_Queen(i):
    global cnt
    if i == N:
        cnt += 1
        return
    for j in range(N):
        if not col[j] and not dia_1[i+j] and not dia_2[N+j-i-1]:
            col[j] = 1
            dia_1[i + j] = 1
            dia_2[N + j - i - 1] = 1
            N_Queen(i+1)
            col[j] = 0
            dia_1[i + j] = 0
            dia_2[N + j - i - 1] = 0

N = int(input())
col = [0]*N
cnt = 0
dia_1 = [0] * (2 * N - 1)   # 상향대각 / i+j
dia_2 = [0] * (2 * N - 1)   # 하향대각 \ n+j-i-1
N_Queen(0)
print(cnt)
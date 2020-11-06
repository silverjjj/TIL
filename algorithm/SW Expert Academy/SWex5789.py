for tc in range(1, int(input())+1):
    N, Q = list(map(int, input().split()))
    result = [0] * N
    cnt = 0
    for i in range(Q):
        L, R = list(map(int, input().split()))
        cnt += 1
        for j in range(L-1,R):
            result[j] = cnt

    result = " ".join(map(str, result))
    print("#{} {}".format(tc,result))
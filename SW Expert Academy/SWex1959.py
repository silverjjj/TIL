T = int(input())

for tc in range(0,T):
    N_limit, M_limit = list(map(int, input().split()))
    N = list(map(int, input().split()))
    M = list(map(int, input().split()))
    result1, result2 = 0, 0
    if len(N) > len(M):
        for i in range(0,len(M)):
            result1 += N[i] * M[i]
            result2 += N[-1-i] * M[-1-i]
            if result1 > result2:
                result = result1
            else:
                result = result2
    elif len(N) < len(M):
        for j in range(0,len(N)):
            result1 += N[j] * M[j]
            result2 += N[-1 - j] * M[-1 - j]
            if result1 > result2:
                result = result1
            else:
                result = result2

    print('#{0} {1}'.format(tc+1,result))
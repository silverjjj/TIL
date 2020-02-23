T = int(input())

for tc in range(T):
    N,M = map(int,input().split())
    n_list=[]
    for i in range(0,N):
        n = list(map(int,input().split()))
        n_list.append(n)

    sum = 0
    sum_list= []
    for k1 in range(0,N-M+1):
        for k2 in range(0,N-M+1):
            for i in range(0,M):
                for j in range(0,M):
                    sum += n_list[i+k1][j+k2]
            sum_list.append(sum)
            sum =0

    print(f'#{tc+1} {max(sum_list)}')
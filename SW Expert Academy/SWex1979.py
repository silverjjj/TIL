T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    n_list = []
    for i in range(0, N):
        n = list(map(int, input().split()))
        n_list.append(n)
    total = cnt = result = 0
    # i는 x고정좌표 j는 y고정 좌표이고
    # x와 y는 변하는값입니다.
    for i in range(N):
        for j in range(N - K + 1):
            for y in range(K):
                total += n_list[i][j+y]
            if total == K:
                cnt += 1        # cnt는 1의 연속적으로 K개있는 갯수
            total = 0

        if cnt == 1:           # cnt가 1개인경우에만 result로 더해줌
            result += 1
        cnt = 0
    for j in range(N):
        for i in range(N - K + 1):
            for x in range(K):
                total += n_list[i+x][j]
            if total == K:
                cnt += 1
            total = 0
        if cnt == 1:
            result += 1
        cnt = 0
    print(f"#{tc+1} {result}")
T = int(input())
for tc in range(1,T+1):
    n,m,l = map(int,input().split())
    node = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        node[a].append(b)
    visit = [0] * (n+1)
    i = n
    while visit[l] != 1:
        # 마지막 번호인 n이 짝수면 단독으로 홀수면 그냥 같이
        if n % 2 == 1:   # 홀수
            node[i//2] = node[i] + node[i - 1]
            visit[i] = 1
            visit[i-1] = 1
        else:   # 짝수면
            if i == n:
                node[i//2] = node[i]
                visit[i] = 1
            elif i < n:
                node[i // 2] = node[i] + node[i + 1]
                visit[i] = 1
                visit[i + 1] = 1
        i -= 2
    print("#{} {}".format(tc,sum(node[l])))

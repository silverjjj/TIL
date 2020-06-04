# SWex5521. 상원이의 생일파티
'''
해당 문제는 상대적으로 쉬운문제였지만
문제에서 말하는건 양방향그래프인데, 단방향 그래프로 착각하여
5번이나 fail을 했음.
문제에서 요구하는점을 정확하게 파악할필요가 있음.
'''
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        a,b = map(int,input().split())
        adj[a].append(b)
        adj[b].append(a)
    # print(adj)
    s = []
    invited = [0]*(N+1)
    invited[1] = 1
    for friend in adj[1]:
        s.append(friend)
        invited[friend] = 1
    while s:
        x = s.pop()
        for i in adj[x]:
            invited[i] = 1
    invited[1] = 0
    print("#{} {}".format(tc,sum(invited)))


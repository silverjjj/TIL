T = int(input())
for tc in range(1,T+1):
    k = int(input())
    case = list(map(int,input().split()))
    visit = [0]*k
    result = []
    def f(n,sum):
        global visit
        if n == k:
            result.append(sum)
            # for i in range(k):
            #     if visit[i] == 1:
            #         sum+=case[i]
            # # print(sum)
            # if sum not in result:
            #     result.append(sum)
        else:
            # visit[n] =1
            f(n+1,sum+case[n])
            # visit[n] = 0
            f(n+1,sum)
    f(0,sum)
    print(set)
    result = set(result)
    print("#{} {}".format(tc,len(result)))
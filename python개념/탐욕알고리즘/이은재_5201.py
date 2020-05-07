T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    # 무게
    weight = list(map(int,input().split()))
    # 트럭적재용량
    truck = list(map(int,input().split()))
    weight.sort(reverse=True)
    truck.sort(reverse=True)
    w = t = sum = 0
    while w != n and t != m:
        # print(w,t,sum)
        flag = True
        while flag:
            if weight[w] > truck[t]:
                w+=1
                flag = False
            elif weight[w] <= truck[t]:
                sum += weight[w]
                w += 1
                t += 1
                flag = False
    print("#{} {}".format(tc,sum))

# SWex5642. [Professional] 합
T = int(input())
for tc in range(T):
    n = int(input())
    num = list(map(int, input().split()))
    maxV = -1234
    if max(num) < 0:
        maxV = max(num)
    else:
        for j in range(n):
            sum = 0
            for k in range(j, n):
                sum += num[k]
                if sum < 0:
                    break
                if sum > maxV:
                    maxV = sum

    print("#{} {}".format(tc + 1, maxV))
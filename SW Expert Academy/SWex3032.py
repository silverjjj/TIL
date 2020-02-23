
T = int(input())
for tc in range(1,T+1):
    A, B = map(int,input().split())
    result = -1
    for y in range(-50,50,1):
        for x in range(-50,50,1):
            if (A*x) + (B*y) == 1:
                result = x, y

    print("#{} {}".format(tc, result))

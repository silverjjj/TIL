T = int(input())
for tc in range(1,T+1):
    points = list(map(int, input().split()))
    result = []
    for i in range(len(points)):
        if points[i] < 40:
            result.append(40)
        else:
            result.append(points[i])

    real_result = sum(result) // len(result)
    print("#{} {}".format(tc,real_result))
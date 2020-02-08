for tc in range(1, 11):
    dump = int(input())
    data = list(map(int, input().split()))
    for i in range(dump):
        data.sort()
        data[0] = data[0]+1
        data[99] = data[99]-1

    data.sort()
    print("#{} {}".format(tc,data[99] - data[0]))
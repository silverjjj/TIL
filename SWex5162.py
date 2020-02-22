for tc in range(1, int(input())+1):
    A, B, C = map(int, input().split())

    if A > B:
        result = C//B
    else:
        result = C//A

    print("#{} {}".format(tc,result))
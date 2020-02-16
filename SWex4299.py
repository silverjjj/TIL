for tc in range(1,1+int(input())):
    D, H, M = map(int, input().split())
    # 분계산
    if M >= 11:
        M = M - 11
    else:
        H = H - 1
        M = M + 60 - 11
    # 시간 계산
    if H >= 11:
        H = H - 11
    else:
        D = D - 1
        H = H + 24 -11

    # 날짜 계산
    if D >= 11:
        D = D - 11
        result = (((D*24)+H)*60)+M
    else:
        result = -1

    print("#{} {}".format(tc,result))
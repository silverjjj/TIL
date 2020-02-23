
for test_case in range(1,T+1):
    P, Q, R, S, W = map(int,input().split(' '))
    result = 0
    if W <= R:
        if Q > P*W:
            result += P*W
        elif Q < P*W:
            result += Q
    elif W > R:
        if (Q +(W-R)*S) > P*W:
            result += P*W
        elif (Q +(W-R)*S) < P*W:
            result += Q +(W-R)*S


    print(f'#{test_case}',result)
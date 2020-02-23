for tc in range(1, 1+int(input())):
    N = input()
    cnt = 0
    result = 'Not exist'
    for i in range(len(N)//2):
        if N[i] == N[-1-i]:
            cnt += 1
    if len(N)//2 == cnt:
        result = 'Exist'
    print("#{} {}".format(tc,result))
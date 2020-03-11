for tc in range(int(input())):
    m = list(map(str,input()))
    n = len(m)
    # print(m)
    cnt = 0
    if m[0] == '1':
        cnt = 1
    for i in range(n-1):
        if m[i] != m[i+1]:
            cnt +=1
    print("#{} {}".format(tc+1,cnt))
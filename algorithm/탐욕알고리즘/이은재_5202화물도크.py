
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [[0]*2 for _ in range(n)]
    for i in range(n):
        arr[i] = list(map(int,input().split()))

    # 끝나는 시간을 기준으로 sort
    arr.sort(key=lambda x:x[1])

    end = arr[0][0] # 시작시간
    cnt = 1
    for i in range(1,n):
        if end <= arr[i][0]:
            end = arr[i][1]
            # print(end)
            cnt +=1
    print("#{} {}".format(tc,cnt))
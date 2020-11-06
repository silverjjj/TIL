#SWex4835 배열 - 구간합

for tc in range(int(input())+1):
    n,m = map(int, input().split())
    arr = list(map(int, input().split()))
    s = 0
    for i in range(m):
        s += arr[i]
    # print(s)
    minV = s
    maxV = s
    # 두번째 구간부터 계산
    for i in range(n-m):
        s += arr[i+m] - arr[i]
        # if maxV < s:
        #     maxV = s
        # elif minV >= s:
        #     minV = s
    # print(s_list)
        maxV = max(maxV,s)
        minV = min(minV,s)
    print("#{} {}".format(tc+1,maxV-minV))
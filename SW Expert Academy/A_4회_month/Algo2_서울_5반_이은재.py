'''
어린이 N명이 사탕을 무작위로 가져감
추가 사탕을 나눠주는데, 어린이들에게 서로 다른 사탕을 1개씩 나눠주며,
어린이들이 가능한 많은 종류를 맛보게 하고싶다.
사탕종류가 어린이보다 적은 경우엔. 앞의 어린이 M명에게만 준다.

어린이명수(N), 사탕종류수(M)(1~M번)
N명의
어린이의 사탕갯수, 번호
3
3 4
4 1 1 2 2
3 1 1 4
3 2 3 4
4 3
3 1 2 3
1 1
3 3 3 2
1 2
2 5
5 1 2 3 4 5
0
'''
def find(k,candys):
    global maxV,result
    if k == n-full:
        result = 0
        for row in candys:
            result += sum(row)
        if result > maxV:
            maxV = result
        return
    if maxV == maxSum:
        return
    for i in range(0,n):  # 사탕을 받는 경우
        for m in range(1, M+1):    # 1~M번까지의 사탕중 줬으면 1로 표시
            if candys[i][m] == 0 and get_candy[i+1] == 0 and send_candy[m] == 0:   # 해당 사탕이 없으면
                get_candy[i] = send_candy[m] = candys[i][m] = 1    # candys의 객체들의 idx = 0 은 사탕을 받았냐 안받았냐의 여부
                find(k+1,candys)
                send_candy[m] = candys[i][m] = get_candy[i] = 0

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    tmp =[]
    for i in range(N):
        arr = list(map(int, input().split()))
        tmp.append(arr[1:])
    tmp_maxV = 0
    if N > M:
        tmp = tmp[:M]
        tmp_maxV = N-M
    n = len(tmp)
    get_candy = [0]*(n+1)     # 1번~ n번까지 애들이 사탕을 받았냐 안받았냐?
    send_candy = [0] *(M+1)    # 1번~ M번 나눠준 사탕
    candys= []
    for lst in tmp:
        used = [0] * (M+1)
        if lst:
            for i in lst:
                used[i] = 1
        candys.append(used)
    full = maxV = 0
    maxSum = tmp_maxV
    for row in candys:
        if M == sum(row):
            full +=1
        maxSum += (sum(row)+1)
    find(0,candys)
    print("#{} {}".format(tc,maxV+tmp_maxV))



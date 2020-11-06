#SWex 5097. [파이썬 S/W 문제해결 기본] 6일차 - 회전
T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    def f(m,k):
        if m == k:
            # print(k)
            return
        else:
            tmp = arr.pop(0)
            arr.append(tmp)
            # print(arr)
            f(m,k+1)
    f(m,0)
    print("#{} {}".format(tc,arr[0]))


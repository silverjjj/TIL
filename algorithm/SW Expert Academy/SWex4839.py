# SWex4839. [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색

for tc in range(int(input())):
    p,a,b= list(map(int,input().split()))
    def f(start,end, key):
        cnt = 0
        while start <= end:
            m = (start + end) // 2
            if m == key:
                return cnt
            elif m > key:
                end = m-1
            else:
                start = m+1

    A = f(1, p,a)
    B = f(1, p,b)
    if A< B:
        result = 'A'
    elif A > B:
        result = 'B'
    elif A==B:
        result = '0'

    print("#{} {}".format(tc+1,result))
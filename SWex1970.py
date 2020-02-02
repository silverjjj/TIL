T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    cnt = []
    m = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    if 10 <= N <= 1000000 and N % 10 ==0:
        for j in range(len(m)):
            A = N // m[j]
            N = N % m[j]
            cnt.append(A)
    print(f'#{test_case}')
    for z in cnt:
        print(z,end = " ")
    print()

T = int(input())
N = int(input())

for test_case in range(1, T+1):
    num = list(map(int, input().split()))
    print(f"#{test_case} ", end=" ")
    if len(num) == N:
        num.sort()
        for i in range(0,len(num)):
            print(num[i], end=" ")
    else:
        0
    print()


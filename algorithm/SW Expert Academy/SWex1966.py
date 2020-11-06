T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n_list = list(map(int,input().split()))
    result = 0
    if len(n_list) == N:
        n_list.sort()
        print(f"#{tc}", end = " ")
        for i in n_list:
            print(i, end =" ")
    print()
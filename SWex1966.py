T = int(input())
N = int(input())
for tc in range(1, T+1):
    n_list = list(map(int,input().split()))
    if len(n_list) == N:
        n_list.sort()
        print(f"#{tc}", end = " ")
        for i in n_list:
            print(i, end = " ")
        print()
    else:
        0
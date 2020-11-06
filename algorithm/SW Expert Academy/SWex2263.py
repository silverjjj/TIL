N = int(input())
if 9 <= N <= 199 and N % 2 == 1:
    num_list = input().split()
    if len(num_list) == N:
        num_list = list(map(int,num_list))
        num_list.sort()
    else:
        0
    print(num_list[N // 2])
else:
    0

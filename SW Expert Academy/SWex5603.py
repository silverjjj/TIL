T = int(input())
for tc in range(1,T+1):
    N = int(input())
    S_list = []
    for _ in range(N):
        S = int(input())
        S_list.append(S)
    result = 0
    avg = sum(S_list) // N
    for i in range(N):
        if S_list[i] > avg:
            result += (S_list[i]-avg)
    print("#{} {}".format(tc,result))
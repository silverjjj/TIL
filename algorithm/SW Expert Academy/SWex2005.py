T = int(input())

for tc in range(1,T+1):
    N = int(input())
    p_list = []
    for i in range(1, N + 1):
        p_list.append([1] * i)
    for i in range(1, N):
        for j in range(1, i):
            p_list[i][j] = p_list[i-1][j-1] + p_list[i-1][j]
    # 숫자형 리스트를 문자형으로 나타내 리스트를 없앰
    print(f"#{tc}")
    for num in range(N):
        print(' '.join([str(i) for i in p_list[num]]))

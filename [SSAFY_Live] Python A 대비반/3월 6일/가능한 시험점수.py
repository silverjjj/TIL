# SWex3752 가능한 시험점수

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))
    s = {0}
    for i in num:
        for j in list(s):
            # print(s)
            s.add(j + i)

    print("#{} {}".format(tc, len(s)))




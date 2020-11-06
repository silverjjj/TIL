#SWex1940. 가랏! RC카!
T= int(input())
for tc in range(1,T+1):
    total = 0
    distance = 0
    currentV = 0
    n = int(input())
    for _ in range(1,n+1):
        c = input().split()

        if len(c) == 1:
            distance += total
        else:
            c[0] = int(c[0])
            c[1] = int(c[1])
            # c 는 command , v는 속도
            if c[0] == 1:
                total += c[1]
            elif c[0] == 2:# 여긴 빼주는곳
                if c[1] > total:#기존의 total보다 큰 c[1]인경우
                    total = 0
                else: # 그게아닌경우
                    total -= c[1]

            distance +=total
    print("#{} {}".format(tc,distance))
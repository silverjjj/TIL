# 문제1 숫자이동

'''
3
5
-1 0 0 10 0 0 3 0 0 10
10
-1 0 0 10 0 0 3 0 0 1
100
-8 -5 3 6 5 -2 5 8 9 -1
'''
T= int(input())
for tc in range(1,T+1):
    N = int(input())
    num = list(map(int,input().split()))
    m = len(num)
    for _ in range(N):
        tmp = [0]*10            # 한바퀴 돌때마다 임시배열 tmp의 모든값을 0으로 정의
        for i in range(m):   # 0 ~ m-1
            if 0 <= abs(num[i]) < 10:     # 절대값이 10보다 작을경우
                if num[i] > 0:      # 양수일때는 -> 오른쪽으로 이동한다.
                    if 0<=i+1<10:     # i+1이 배열내에 있으면
                        tmp[i+1] = tmp[i+1]+num[i]  # tmp[i+1]위치와 num[i]를 더해준다
                    elif i == 9:                  # 배열 밖으로 가면(배열을 벗어날 i값은 9가 유일함)
                        tmp[i] = tmp[i]-num[i]      # tmp[i+1]과 -num[i]를 더해준다. (배열을 벗어나면 부호가 바뀌므로 -을 붙여줌)
                elif num[i] < 0:        # 음수면 <- 왼쪽으로
                    if 0 <= i - 1 < 10:      # i-1이 배열내에 있으면
                        tmp[i-1] = tmp[i-1] + num[i]       # tmp[i-1]에 tmp[i-1]와 num[i]를 더해준다
                    elif i == 0:                          # 배열을 벗어날경우는 i=0이 유일
                        tmp[i] = tmp[i]-num[i]          # tmp[i]에 tmp[i]와 -num[i]를 더해준다.
            elif abs(num[i]) >= 10:       # 절댓값이 10보다 클떄
                if 0<=i-1<10 and 0<=i+1<10:             # 절댓값이 10보다 크고 i+1과 i-1이 배열 내에 있는경우에는
                    tmp[i-1] = tmp[i-1]-abs(num[i])//2       # i 기준으로 오른쪽은 abs(num[i])//2과 왼쪽은-abs(num[i])//2을 더해준다
                    tmp[i+1] = tmp[i+1]+abs(num[i])//2
                elif i == 0:                                # i=0일때와 i=9일때는 각각 i-1과 i+1이 배열리스트 범위를 벗어난다.
                    tmp[0] = tmp[0] + abs(num[i]) // 2      # 그래서 각각 임의로 값을 지정해줘야한다.
                    tmp[1] = tmp[1] + abs(num[i]) // 2
                elif i == 9:
                    tmp[9] = tmp[9]-abs(num[i]) // 2
                    tmp[8] = tmp[8]-abs(num[i]) // 2

        num = tmp                                           # 이것이 핵심이다. -> 한바퀴를 돌고난뒤 값을 tmp에 저장시켜놨는데,
                                                            # 다시 돌기 위해선 tmp값을 num에 저장시켜놓고 tmp의 모든값을 0으로 다시 만든뒤
                                                            # tmp에 다시 값을 할당시켜준다
    print("#{}".format(tc), end = " ")                      # 출력
    for j in range(len(num)):
        print(num[j],end = " ")
    print()
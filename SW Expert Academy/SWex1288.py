T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    if 1 <= N <= 10000000:
        cnt = 0
        a = list()
        while len(a) != 10: # a의 문자길이가 10이 아닐때 까지 반복
            cnt +=1
            N2 = N * cnt    # 숫자 N의 배수를 N2에 저장한다.
            house = list(str(N2))   # N2를 문자열로 변환한뒤 리스트에 저장
            for item in house:      # house에 있는 값을 한개씩 for을 통해 내림
                if item not in a:   # a안에 item가 없으면 리스트 a 에 추가
                    a.append(item)
    else:
        0

    print(f'#{test_case} {cnt*N}')
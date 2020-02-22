T = int(input())
for tc in range(1, T+1):
    N = int(input())
    case = list(map(str, input().split()))
    # N이 짝수면 딱 반으로 나누고 홀수면 나눈후 +1
    if N % 2 ==1: N1 = N//2 +1
    else: N1 = N//2
    case_1 = []
    case_2 = []
    #case_1과 case_2를 이용해 part나누기
    for i in range(N1): case_1.append(case[i])
    for i in range(N1,N): case_2.append(case[i])
    # len 길이에 따라 result과정 설정
    result = []
    if len(case_1) == len(case_2):
        for i in range(N1):
            result.append(case_1[i])
            result.append(case_2[i])
    else:
        for i in range(N1-1):
            result.append(case_1[i])
            result.append(case_2[i])
        result.append(case_1[-1])
    result = " ".join(result)
    print("#{} {}".format(tc,result))
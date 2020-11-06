# for i in range(10):  # 총 10개의 case를 반복 시행
#     a = int(input())  # case길이가 주어진다.
#     case = list(map(int, input().split()))  # 리스트를 이용하여 건물의 층을 받습니다.
#     result = 0
#     for k in range(4, a):  # 처음 counting이 가능한 인덱스 부터 시작 하나씩 시작합니다. 기준이 되는 인덱스로 부터 왼쪽 오른쪽 2개씩이라 5개씩 끊어서 생각햇습니다.
#         if case[k - 2] > case[k] and case[k - 2] > case[k - 1] and case[k - 2] > case[k - 3] and case[k - 2] > case[
#             k - 4]:  # 기준이 되는 부분case[k-2]가 가장 크면 조망이 확보되는 층을 갖고 있으므로
#             b = sorted(case[k - 4:k + 1])  # 정렬을 통해 가장 큰 층에서 그다음 큰 층을 빼서 result값에 계속해서 누적 시켜 나간다.
#             result += b[4] - b[3]
#
#     print(f'#{i + 1} {result}')  # output 형식에 맞게 출력했습니다.


#
# for test_case in range(10):                     # test_case를 10개로 둔다
#     gil2 =int(input())                          #길이를 gil2로 두고
#     case = list(map(int,input().split()))
#     if gil2 <= 1000 and case <=255:
#         result = 0
#         for i in range(2, gil2):
#             if case[i] > case[i-2] and case[i] > case[i-1] and case[i] > case[i+1] and case[i] > case[i+2]:
#                 sum = sorted(case[i-2:i+3])
#                 result += sum[4]-sum[3]
#         print("#{0} {1}".format(test_case+1,result))
#

for test_case in range(10):                     # test_case를 10개로 둔다
    gil2 =int(input())                          # 길이를 gil2로 두고
    case = list(map(int,input().split()))       # 빌딩을 여러개 건설한다.
    if gil2 < 1001:                            # 길이를 1000안넘게 하고 넘으면 break
        result = 0
        for i in range(2, gil2-1):                # 3번째 자리에서 gil2까지를 기준으로 하여
            if case[i] > case[i-2] and case[i] > case[i-1] and case[i] > case[i+1] and case[i] > case[i+2]: #본인 기준 왼쪽 2개, 오른쪽 2개 보다 큰걸 걸러낸다
                sum = sorted(case[i-2:i+3])         # 걸러진 5개의 수를 sorted하여 sum으로 할당
                result += sum[4]-sum[3]             # 할당된 모든 sum들은 sorted된 숫자중에서 가장큰수 - 두번째로 큰수를 하여 result에 할당
        print("#{0} {1}".format(test_case+1,result))
    else:
        break
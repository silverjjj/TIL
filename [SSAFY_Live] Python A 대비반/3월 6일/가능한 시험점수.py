#SWex3752 가능한 시험점수
# 부분집합을 이용해서 품 -> 제한시간 오류
def f(i,N):   #i번째 원소를 포함하는 경우/ 아닌경우 -> 재귀호출
    global bit
    global num
    global result
    # print(result)
    if i == N:

        result.append(bit)
        return
    else:
        f(i + 1, N)
        # print(bit)
        bit[i] = 1        # i 번째 원소 선택된경우
        f(i + 1, N)
        bit[i] = 0          # i 번


T= int(input())
for tc in range(1,T+1):
    N = int(input())
    num = list(map(int,input().split()))
    bit = [0]*N
    result = []
    f(0, N)  # 부분집합을 구하고 -> 총합이 10인 부분집합갯수 세기
    # result = set(result)
    print(result)
    # print("#{} {}".format(tc,len(result)))






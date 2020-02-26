#i번째 원소를 포함하는 경우/ 아닌경우 -> 재귀호출
# 완전탐색으로 풀었음 -> 시간이 많이 나옴
def f(i,N,B):    # B이상의 값중 가장작은걸 출력
    global bit
    global result
    print(visited)
    if i == N:      # base case : bit배열의 모든칸이 결정됨
        sum = 0       # sum
        for j in range(N):
            if visited[j] == 1:
                sum += bit[j]   #선택된 원소의 누적값
        if sum >= B:      # 누적합이 K=10 과 같다면 카운팅함.
            result.append(sum)
        return
    else:
        visited[i] = 1        # i 번째 원소 선택된경우
        f(i + 1, N, B)
        visited[i] = 0          # i 번째 원소 선택 안된경우
        f(i + 1, N, B)
T = int(input())
for tc in range(1,T+1):
    N ,B= list(map(int,input().split()))    #5, 16
    bit = list(map(int,input().split()))
    visited = [0]*N
    result = []         # 조건을 만족하는 부분집합의 갯수
    f(0,N,B)    # 부분집합을 구하고 -> 총합이 10인 부분집합갯수 세기
            #  N은 원소수, K는 부분집합의 합 EX.(1,2,8) 같은거
    print("#{} {}".format(tc,min(result)-B))
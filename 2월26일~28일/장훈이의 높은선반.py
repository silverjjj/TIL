#i번째 원소를 포함하는 경우/ 아닌경우 -> 재귀호출
# 완전탐색으로 풀었음 -> 시간이 많이 나옴
# 백트래킹으로 풀면 잘풀릴듯
'''
1
5 16
1 3 3 5 6
'''
def f(i,N,B):    # B이상의 값중 가장작은걸 출력
    global bit
    global result
    print(visited)
    if i == N:
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
    result = []
    f(0,N,B)
    print("#{} {}".format(tc,min(result)-B))
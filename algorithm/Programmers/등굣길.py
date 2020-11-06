# 이 문제는 문제내에 1000000007로 나눠라 라는 말이 있기 때문에
# 효율성 측면에서 굉장히 메모리가 큰 문제임을 알수있다.
# 처음엔 bfs를 생각해봤지만, 그렇게 풀면 시간초과가 나올듯 싶어 DP를 생각했다.
def solution(m, n, puddles):
    answer = 0
    mapping = [[0]*(m+1) for _ in range(n+1)]
    mapping[1][0] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if [j,i] in tuple(puddles):
                mapping[i][j] = 0
            else:
                mapping[i][j] = (mapping[i-1][j] + mapping[i][j-1])
    answer = mapping[n][m] % 1000000007
    return answer
m = 4
n = 3
puddles	=[[2, 2]]
solution(m, n, puddles)
# SWex 1865 동철이의 일 분배
# 순열을 활용한 문제
def dfs(x, s):
    global arr
    global maxV
    global used
    if s <= maxV or s == 0:  #  s < maxV : s가 곱해다가다 maxV보다 낮으면 그 윗자리 n-1로 다시 돌아가
        return               # 확률인 s는 곱해나갈수록 작아진다.
    if x == N:          # 모든 used에 배정이 된경우
        if maxV < s:        # 지금까지 구해온 s 가 기존의 maxV보다 클경우
            maxV = s        # maxV 를 s 로 한다.

    for i in range(N):
        if used[i] == 0:
            used[i] = 1
            dfs(x + 1, s * (arr[x][i]) * 0.01)
            used[i] = 0  # k 번째 사람이 다른일을 맡을수 있게 해준다.


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    used = [0] * N
    maxV = 0
    dfs(0, 1)
    print("#{} {:.6f}".format(tc, maxV * 100))
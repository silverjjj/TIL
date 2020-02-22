# 재귀로 풀어야함.. 어려워서 좀다 개념학습후에 풀자
def go(idx, score, cal):    # 인덱스, 맛점수, 칼로리
    global ans, N, L     # 전역에 있는 변수를 지역에서 사용가능토록,
    if idx == N:    #인덱스 갯수
        ans = max(ans, score)
        return

    s, c = data[idx] #data는 s,c가 들어가있는 리스트 거기에서 idx(0~4)를하여 sc를 불러온다
    if cal + c <= L:   # cal = 0, c =
        go(idx + 1, score + s, cal + c)
    go(idx + 1, score, cal)


T = int(input())
for case in range(1, T + 1):
    N, L = map(int, input().split())
    data = []
    for _ in range(N):
        s, c = map(int, input().split())
        data.append((s, c))     #s,c는 맛점수랑 칼로리..
    ans = 0
    go(0, 0, 0) # idx, score, cal 을 0 0 0 으로 함수 시작

    print("#%d" % (case), ans)
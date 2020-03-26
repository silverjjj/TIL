#SWex1219 [S/W 문제해결 기본] 4일차 - 길찾기 dfs 기본문제
for _ in range(10):
    tc,c = map(int,input().split())
    G = [[] for _ in range(100)]            # dfs를 사용하기전 각각의 방문위치를 저장하기 위한 100개의 비어있는 배열
    num = list(map(int,input().split()))
    for i in range(0,c*2,2):
        G[num[i]].append(num[i+1])          # 각각의 위치에 맞게 향하는곳을 지정
    visit = [0]*100                         # 한번 방문한곳은 다시 방문안하려고 만든 visit 배열
    s = []
    v = 0
    s.append(v)
    result = 0
    while s:                        # len(s) == 0 일때 나옴 -> 못찾았을떄
        for w in G[v]:              # v번째 배열에 있는 방문한 위치인 W로 감
            if w == 99:             # w == 99면 도착한의미
                result = 1
                break               # for문을 빠져나옴
            if visit[w] == 0:       # 방문하지 않았다면
                s.append(w)         # 그 위치를 스택에 푸쉬
                visit[w] = 1        # 방문표시
                v = w               # 방문한 w을 v로 하여 v기준으로 다시 출발
                break               # for문을 빠져나감
        else:               # 방문한 위치를 다 스택에 넣거나 방문할 위치가 없으면
            v = s.pop()     #  다시 시작점을 찾기위해 스택하여 v로 할당

                            # 위 과정을 계속해서 반복
        if result == 1:     # result == 1 다시말해서 w에 도착하면 while을 빠져나옴
            break

    print("#{} {}".format(tc,result))
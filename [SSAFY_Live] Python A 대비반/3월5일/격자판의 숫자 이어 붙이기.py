#SWex2819 격자판 이어 붙이기
# append, pop 으로 풀고 리스트result에 넣어 겹치는걸 빼는 알고리즘으로 품 -> 3초 나옴
# set을 이용해서 겹치는걸 한방에 빼버림 -> 0.3초
dx = [-1,0,1,0] # 상 우 하 좌
dy = [0,1,0,-1]
def f(x,y,rm):
    global result
    # print(rm)
    if len(rm) == 7:
        result.add(rm)
        return
    else:
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx >= 0 and nx < 4 and ny >= 0 and ny < 4:
                f(nx, ny, rm + room[nx][ny])

T = int(input())
for tc in range(1,T+1):
    room = [list(map(str,input().split())) for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            f(i, j, room[i][j])
    print("#{} {}".format(tc,len(result)))

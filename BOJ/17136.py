# 백준_17136
# 유망성검사
def promising(x,y,paper):
    for nx in range(x,x+paper):
        for ny in range(y,y+paper):
            # print(room[nx][ny])
            if 0<=nx<10 and 0<=ny<10:
                if room[nx][ny] != 1:
                    return False
            else:
                return False
    return True

def dfs(depth):
    global result, stan_result, minV
    # paper가 1~6부터 차례대로 깊이우선탐색을 진행
    # 종이에서 1을 찾는다.
    if depth >= minV and minV > 0:
        return
    if result == stan_result:
        minV = depth
        return
    for i in range(10):
        for j in range(10):
            if room[i][j] == 1:
                break
        if room[i][j] == 1:
            break
    # print(i,j)
    for paper in range(1,6):
        # 유망성 검사 통과시 해당 paper를 갯수를 -1 해줌
        used_paper = []
        if paper_cnt[paper]:
            if promising(i, j, paper):
                paper_cnt[paper] -=1
                for ni in range(i,i+paper):
                    for nj in range(j,j+paper):
                        if 0 <= ni < 10 and 0 <= nj < 10:
                            room[ni][nj] = 0   # 붙이기 진행
                            used_paper.append([ni,nj])    # 임시 저장
                result += paper**2
                dfs(depth+1)
                paper_cnt[paper] +=1
                result -= paper ** 2
                # print(used_paper)
                for x,y in used_paper:
                    # print(x,y)
                    room[x][y] = 1

room = [list(map(int,input().split())) for _ in range(10)]
paper_cnt = [0,5,5,5,5,5]   # 1~5의 색종이의 갯수
stan_result = 0
result = 0
minV = -1
for row in room:
    stan_result += sum(row)
if stan_result >= 4:
    dfs(0)
else:
    minV = stan_result
print(minV)
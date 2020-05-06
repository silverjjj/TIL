# 프로그래머스_완전탐색_카펫
def solution(brown, red):
    # x*y = brown+red
    # xy -2x-2y+4 = red
    # 2x+2y = 4+brown 이다. 완전탐색을 통해 풀자
    answer = []
    for x in range(brown):
        for y in range(brown):
            if 2*x+2*y == 4+brown:
                if x >= y and x>=3 and y>=3:
                    if x*y == brown+red:
                        answer.append([x,y])
    a = answer[0]
    return a

brown = 24
red = 24
print(solution(brown,red))
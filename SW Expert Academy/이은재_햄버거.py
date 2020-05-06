#SWex5215
# 조합을 이용한 문제
# 하지만 중간중간에 조건을 걸어 시간, 메모리를 줄여준다.
def gogo(idx,score,cal): # 인덱스, 점수, 칼로리
    global maxV
    if idx == n:
        # print(visit)
        if cal <=l:
            if score > maxV:
                maxV = score
    elif cal > l:
        return
    elif cal == l:
        if score > maxV:
            maxV = score
    else:
        s,c = case[idx]     # case 0~n까지 각각의 재료와 칼로리가 있음.
        # visit[idx] = 1
        gogo(idx+1,score+s,cal+c)
        # visit[idx] = 0
        gogo(idx+1, score, cal)

for tc in range(int(input())):
    n, l = map(int,input().split())
    case = [list(map(int,input().split())) for _ in range(n)]
    # print(case)
    maxV = 0
    # visit=[0]*n
    gogo(0,0,0) # idx, score, cal 이 0부터 시작
    print("#{} {}".format(tc+1,maxV))

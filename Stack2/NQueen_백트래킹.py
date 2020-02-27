def promissing(level):
    for i in range(1,level):    #이제까지 놓여진 말 확인 (1~level-1)
        #현재놓여진 말의 정보 cols[level]
        #이제까지 놓여진 말의 정보 cols[i]
        #같은 열이면 X, 대각선이어도 X
        if cols[i] == cols[level] or (level - i) == abs(cols[i] - cols[level]):
            return False
    return True
def queen(level):
    global cnt
    if promissing(level) == False:  #유망성 검사
        return                      #검사후 가망이 없으면 이전으로 리턴
    elif level == N:                #현재 레벨이 마지막행이라면
        cnt = cnt+1                 #카운팅 늘리기
        return
    else:
        for i in range(1,N+1):
            cols[level+1] = i       #다음행 확인하기 : 다음행에 i 넣고
            queen(level+1)          #재귀호출   -> 재귀에서 돌아오면 다시 반복 (i증가)
        return
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cols = [0] * (N+1)  #1~N 행의 열 정보 저장
    cnt = 0
    queen(0)
    print("#{} {}".format(tc,cnt))
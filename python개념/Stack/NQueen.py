def check(d):
    for i in range(1,d):
        if cols[i] == cols[d] or (d-i) == abs(cols[i] - cols[d]):
        # d =2 일때 i는 1 -> cols[1] == cols[2]는 1행과 2행이 같으면 false한다는 의미 (같다는 의미는 같은열에 위치한다.)-> 놓이면 안된다.
        # (i-d) == abs(cols[i] - cols[d]) 의미는 행끼리 뺀것과 열끼리 뺀것이 같으면 false
        # i와 d는 행을 cols[i]와 cols[d] 각각 i행의 열과 d행의 열을 의미
            return False
    return True
def nqueen(d):
    global cnt
    if check(d) == False:   # 2행에서 검사(퀸이 놓여질수 있는 위치인가 아닌가?)하기 위해 check 함수
        return
    elif d == n:
        cnt +=1
        return
    else:
        for i in range(1, n+1):
            cols[d+1] = i          #d= 0에서 i= 1일때 cols[1] = 1로 저장되어
                                    #   cols[1]은 1행 의미  =1 은 1열을 의미
            nqueen(d+1)         # 1행 1열에 퀸을 넣고 2행으로 보내본다.
        return

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    cnt = 0
    cols = [0]*(n+1) # 1~n행 까지의  열정보 저장
    nqueen(0)
    print("#{} {}".format(tc,cnt))

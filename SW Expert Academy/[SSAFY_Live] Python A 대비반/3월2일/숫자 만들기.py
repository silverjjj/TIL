'''
10
5
2 1 0 1
3 5 3 7 9
6
4 1 0 0
1 2 3 4 5 6
'''
def f(n,k,r,op1,op2,op3,op4): #계산에 사용할숫자, 배열의 크기, 이전까지의연산 결과
    global minV, maxV
    if n == k:
        if maxV < r:
            maxV = r
        if minV > r:
            minV = r
    else:
        if op1 > 0:
            f(n+1, k, r+card[n], op1-1, op2, op3, op4)      # -1하는 이유는 한개씩 줄여나가는것
        if op2 > 0:
            f(n+1, k, r-card[n], op1,op2-1,op3,op4)
        if op3 > 0:
            f(n+1, k, r*card[n], op1, op2, op3-1, op4)
        if op4 > 0:
            f(n+1, k, int(r/card[n]), op1,op2,op3,op4-1)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    op1,op2,op3,op4 = map(int,input().split())
    card = list(map(int,input().split()))
    minV = 10000000000
    maxV = -10000000000
    f(1, N, card[0], op1, op2, op3, op4)
    print("#{} {}".format(tc, maxV-minV))
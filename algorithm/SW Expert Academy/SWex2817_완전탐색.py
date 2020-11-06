# 백트래킹을 이용한 수열의 합 구하기
'''
1
4 3
1 2 1 2
'''
def f(i,N,K):    # N은 부분집합의 갯수 , K은 부분집합의 합
                # N = 4, K = 3 << 부분집합의 합이 3이 되는 갯수
    global bit
    global cnt
    if i == N:
        sum = 0
        for j in range(len(bit)):
            if bit[j] == 1:
                sum += A[j]
        if sum == K:
            cnt +=1
        return

    else:
        bit[i] = 1
        f(i+1,N,K)
        bit[i] = 0
        f(i+1,N,K)

T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    bit = [0]*N
    cnt = 0
    f(0,N,K)
    print("#{} {}".format(tc,cnt))
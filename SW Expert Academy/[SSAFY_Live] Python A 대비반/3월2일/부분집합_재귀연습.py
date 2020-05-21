# 부분집합의 합
# 서로다른 k개의 자연수 집합에서 부분집합 원소의 합이 M인경우
def f(n,k,s,M):
    global cnt
    if s == M:
        cnt +=1
        return
    elif n == k:
        return
        # 결정이 된거면 s를 return
    else:
        f(n+1,k,s+A[n],M)   # 부분집합에 A[n] 포함
        f(n+1,k,s,M)        # 미포함
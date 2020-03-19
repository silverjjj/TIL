arr = 'ABC'
N = len(arr)
bit = [0]*N

# 재귀를 이용한 부분집합
def subset(k, n):    # k :함수호출의 깊이, n : 호출트리의 높이, 단말노드드
    if k == n:
        print(bit)
        return
    # return을 해도되고 안해도된다. why ?? 어차피 어떠한 조건하에 재귀가 다 실행되고 더이상 할것이 없을떄 되돌아감.
    else:
        bit[k] = 0
        subset(k+1,n)
        bit[k] = 1
        subset(k+1,n)
subset(0,3)
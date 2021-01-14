
def solution(n):
    if n < 3:
        return n
    else:
        pivo = [0]*(n+1)
        pivo[1],pivo[2] = 1, 2
        for idx in range(3,n+1):
            pivo[idx] = (pivo[idx-1] + pivo[idx-2]) % 1234567
        return (pivo[-1]%1234567)

n = int(input())
solution(n)
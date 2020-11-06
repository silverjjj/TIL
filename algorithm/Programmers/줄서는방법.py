def solution(n, k):
    answer = []
    arr = [i for i in range(1,n+1)]
    while n > 0:
        N = 1
        for i in range(n-1, 0, -1):
            N *= i
        share = (k//N)
        k -= (N*share)

        if k == 0:
            share -= 1
        answer.append(arr[share])
        arr.remove(arr[share])
        n -= 1
    return answer
n = 5
for k in range(1,10):
    solution(n, k)
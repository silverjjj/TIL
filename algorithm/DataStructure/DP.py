'''
DP(Dynamic Programming)
DP(동적계획)알고리즘은 입력크기가 작은 부분을 해결한뒤
그 해를 이용하여 보다 큰 크기의 부분문제들을 해결하여,
최종적으로 문제를 해결하는 알고리즘
```
```
파보나치 수의 DP적용
1) 부분 문제로 나누는일이 끝났으면, 가장 작은부분문제부터 해를 구한다.
2) 그 결과는 테이블에 저장하고, 테이블에 저장된 부분문제의 해를 이용하여 상위문제의 해를 구한다.
'''
'''
f[1]과 f[2]를 구해놓고 이를 배열 f에 넣어
for 문을 이용해 f배열을 채워나간다.. 이때 피보나치 수열공식은 
f[i] = f[i - 1] + f[i - 2]

'''
def fibo_iter(n):
    f = [0] * (n+1)
    f[1] = f[2] = 1         #기저사례
    for i in range(2,n+1):   # i는 문제를 식별하는 값
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

n = 1
print(fibo_iter(n))

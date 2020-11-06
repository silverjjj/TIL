# SWex4869 종이붙이기
'''
2 * 1 타일을 2 * N 공간에 붙이는 경우의수 f(N)

f(N)은
맨 왼쪽에 세로로 1개 붙이고 남은 f(N-1)
맨 왼쪽에 가로로 2개 붙이고 남은 f(N)
'''
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    n = N//10
    def f(n):
        if n < 2:
            return 1
        else:
            return f(n-1) + 2 * f(n-2)

print("#{}".format(tc,f(n)))

#for 문으로 구현하기
F = [0]*31
F[1] = 1
F[2] = 3
for i in range(3,31):
    F[i] = F[i-1] + 2 * F[i-2]
for tc in range(1,T+1):
    N = int(input())
    print("{}{}".format(tc,F[N])
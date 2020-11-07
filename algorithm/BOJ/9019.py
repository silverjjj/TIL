'''
BOJ 9019

n은 0이상 9999이하의 숫저

D : n을 두배, 9999보다 크면 10000으로 나눔
S : n --> n-1로 저장 n이 0이면 9999로
L : 각자릿수를 왼편으로 회전, 1234 --> 2341
R : 각 자릿수롤 오른편으로 회전, 1234 --> 4123
'''
from collections import deque
import sys
input = sys.stdin.readline
def D_level(n):
    n = (n * 2)%10000
    return n

def S_level(n):
    if n == 0:
        n = 9999
    else:
        n -= 1
    return n

def L_level(n):
    return int((n % 1000 * 10) + (n / 1000))

def R_level(n):
    return int(n % 10 * 1000 + n // 10)

T = int(input())
for _ in range(T):
    A, B = map(int,input().split())
    visited = [0]*10000
    visited[A] = 1
    dq = deque([[A,'']])
    res = ''
    while dq:
        n, char = dq.popleft()
        if n == B:
            res = char
            break

        D_num = D_level(n)
        if not visited[D_num]:
            visited[D_num] = 1
            dq.append([D_num, char + 'D'])

        S_num = S_level(n)
        if not visited[S_num]:
            dq.append([S_num,char+'S'])
            visited[S_num] = 1

        L_num = L_level(n)
        if not visited[L_num]:
            dq.append([L_num,char+'L'])
            visited[L_num] = 1

        R_num = R_level(n)
        if not visited[R_num]:
            visited[R_num] = 1
            dq.append([R_num,char+'R'])

    print(res)
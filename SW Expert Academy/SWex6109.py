# SWex6109. 추억의 2048게임
def f(N,rm):
    for i in range(N):
        for j in range(N):
            rm[i][j] = rm[j][i]
def go(N,rm):
    # s = []
    # s1 = []
    # for i in range(N):
    #     for j in range(N):
    #         s.append(rm[i][j])
    #
    #     if s[-1] == s[-2]:
    #         s1.append(s[-1]*2)
    #         s.pop()
    #         s.pop()
    #     else:
    #         s1.append(s[-1])
    #

n = input().split()
N= int(n[0])
S= n[1]
rm = [list(map(int,input().split())) for _ in range(N)]
for row in rm:
    print(row)
if S =='Right':
    go(N,rm)
elif S=='Up':
    rm = f(N,rm)
    go(N,rm)

elif S == 'Left':
    rm = f(N,rm)
    rm = f(N,rm)
    go(N,rm)
elif S == 'Down':
    rm = f(N,rm)
    rm = f(N,rm)
    rm = f(N,rm)
    go(N,rm)


'''
BOJ 1107
'''

def diff(char_P):
    global minV
    num = abs(int(N) - int(char_P)) + len(char_P)
    if minV > num:
        minV = num

def perm(n,i):
    if n == i:
        char_P = "".join(P)
        diff(char_P)
        return
    else:
        for j in range(K):
            P[n] = remote[j]
            # P += remote[j]
            perm(n+1,i)

N = str(input())
M = int(input())
removes = []
# res = [abs(int(N) - 100)]
minV = abs(int(N) - 100)
if minV != 0:
    if M != 0:  # 1~ 9일땐 제거를 받고
        removes = list(map(str,input().split()))
    remote = ['0','1','2','3','4','5','6','7','8','9']
    for num in removes:
        remote.remove(num)
    K = len(remote)
    if M == 0:
        if minV > len(N):
            minV = len(N)
    elif M == 10:
        pass
    else:
        for i in range(1,len(N)+2):
            print(i, minV)
            P = [0] * i
            perm(0,i)
print(minV)
'''

99899
1 99899
2 99899
3 99899
4 99003
5 90004
6 5
5

1 99899
2 99899
3 99899
4 99891
5 98892
6 88893
11118


99999
9
0 2 3 4 5 6 7 8 9
'''
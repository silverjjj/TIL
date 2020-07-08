# 13458_시험감독
import math
N = int(input())
A = list(map(int,input().split()))
B,C = list(map(int,input().split()))
cnt = 0
for i in range(N):
    cnt +=1
    if A[i] - B >= 0:
        A[i] -= B
    else:
        A[i] = 0
for j in range(N):
    cnt += math.ceil(A[j] / C)
print(cnt)
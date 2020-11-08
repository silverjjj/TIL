'''
BOJ 11652
딕셔너리의 특징 사용
dict
'''
import sys
input = sys.stdin.readline
dict = {}
N = int(input())
for _ in range(N):
    num = int(input())
    if dict.get(num) == None:
        dict[num] = 1
    else:
        dict[num] += 1

maxV, res = 0, float('inf')
for key, val in dict.items():
    if val > maxV:
        res = key
        maxV = val
    elif val == maxV:
        maxV = val
        if res > key:
            res = key

print(res)
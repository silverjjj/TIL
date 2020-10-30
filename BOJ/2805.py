'''
BOJ 2805 이분탐색
36% 시간초과
'''
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
trees = list(map(int,input().split()))
left = 0
right = max(trees)
maxV = 0
while left <= right:
    mid = (left + right) // 2
    res = 0
    for tree in trees:
        if tree > mid:
            res += (tree - mid)
    if res == M:
        maxV = mid
        break
    elif res < M:
        right = mid - 1
    else:           # 자른 나무가 목표보다 크거나 같을때
        left = mid + 1
        if mid > maxV:
            maxV = mid
print(maxV)
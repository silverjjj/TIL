'''
BOJ 10815
'''
import copy, sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
M = int(input())
tmp = list(map(int,input().split()))
visited = ['0']*M
target = copy.deepcopy(tmp)
target.sort()
for i in range(N):
    num = arr[i]
    right = M-1
    left = 0
    while left <= right:
        mid = (right + left) // 2
        if target[mid] == num:
            idx = tmp.index(target[mid])
            visited[idx] = '1'
            break
        if num > target[mid]:
            left = mid + 1
        else:
            right = mid - 1
print(" ".join(visited))
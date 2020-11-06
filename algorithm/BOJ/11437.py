'''

idx가 son
value가 부모
긜고 x,y 순서가 부모 자식이 아님
단 해당 num가 등장하려면 부모가 있어야함 << 이거 아닐수도 있음 주의
'''
import sys
input = sys.stdin.readline
N = int(input())
arr = [0 for _ in range(N+1)]
arr[1] = -1
for _ in range(N-1):
    x,y = map(int,input().split())
    if not arr[y]:
        arr[y] = x
    else:
        arr[x] = y
nums = []
res = []
M = int(input())
for _ in range(M):
    i,j = map(int,input().split())
    nums.append([i,j])

for i, j in nums:
    # print(i,j)
    up_node = [i]
    while i != -1:
        i = arr[i]
        up_node.append(i)
    # print(up_node)
    while j not in up_node:
        j = arr[j]
    print(j)
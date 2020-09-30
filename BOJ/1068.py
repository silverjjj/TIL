'''
5 노드 갯수
-1 0 0 1 1  노드 0 ~ 4번노드
2
'''
import sys
from collections import deque
read = sys.stdin.readline
n = int(input())
arr = list(map(int, read().split()))
rm = int(input())
parent = [[] for _ in range(n)]
visited = [0]*n
for idx, val in enumerate(arr[1:]):
    parent[val].append(idx+1)
q = deque()
q.append(rm)
while q:
    cur = q.popleft()
    for num in parent[cur]:
        q.append(num)

# tree = [[] for _ in range(n)]
# visited = [0]*n
# visited[rm] = 1
# for i in range(1,n):
#     num = arr[i]
#     tree[num].append(i)
#
# q = [0]
# res= 0
# while q:
#     number = q.pop(0)
#     for char in tree[number]:
#         if not visited[char]:
#             visited[char] = 1
#             q.append(char)
#             if len(tree[char]) == 0:
#                 res += 1
# print(res)

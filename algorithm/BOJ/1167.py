'''
1. 리프노드가 없는 정점을 찾자
2. 해당 정점을 root노트라 가정하고 다익스트라를 통해 가장 멀리 있는 정점을 찾자
3. 정점을 찾으면 해당 정점에서 가장 멀리 있는 정점까지의 거리를 측정하자
'''
import sys
from collections import deque
input = sys.stdin.readline

def dijkstra(node):
    dq = deque([])
    dq.append([node,0])
    weight = [0] * (N+1)
    weight[node] = -1
    while dq:
        cur_node,cur_w = dq.popleft()
        for next_node,next_w in tree[cur_node]:
            if not weight[next_node]:
                weight[next_node] += (cur_w + next_w)
                dq.append([next_node, cur_w + next_w])
    maxV = max(weight)
    root = weight.index(maxV)
    return root, maxV
N = int(input())
tree = {}
for _ in range(N):
    arr = list(map(int,input().split()))
    cur = arr[0]
    if cur in tree:
        pass
    else:
        tree[cur] = []
    for i in range(1,len(arr)-1,2):
        tree[cur].append([arr[i],arr[i+1]])
root = -1
for key, val in tree.items():
    if len(val) == 1:
        root = key
        break
root, maxV = dijkstra(root)
root, maxV = dijkstra(root)
print(maxV)
'''
해당 문제는 트리의 노드순서도 다르고 루트노드가 2개 이상일수도있다
지워야할 노드가 tree구현 단계부터 제외시키고, 해당 노드가 부모노드일경우 tree구현에서 제외한다.
트리의 핵심은 위에서 내려오는 입력은 1개지만, 출력은 2개 이상이 된다는점이다. 이점을 주의하고 트리문제를 풀어나가자
'''
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
nodes = list(map(int,input().split()))
M = int(input())
tree = {}
cnt = 0
for i in range(N):      # i가 자식노드, nodes[i]가 부모노드
    if i == M or nodes[i] == M:
        continue
    if nodes[i] in tree:
        tree[nodes[i]].append(i)
    else:
        tree[nodes[i]] = [i]
dq = deque([])
if -1 in tree.keys():
    dq.append(-1)            # root노드 제외한 노드가 지워진경우
while dq:
    cur_node = dq.popleft()
    if cur_node not in tree:
        cnt += 1
        continue
    dq += tree[cur_node]
print(cnt)
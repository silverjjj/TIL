'''
BOJ1525
1. 딕셔너리를 활용해서 방문기능활용
2. 리스트의 메모리를 줄이기위해 2차원이 아닌 1차원 배열 사용
'''
from collections import deque
d = [(0,1),(0,-1),(1,0),(-1,0)]

def BFS(num):
    dq = deque([])
    dq.append(num)
    while dq:
        char = dq.popleft()
        if char == '123456780':
            return dist[char]
        idx = char.index('0')
        x = idx // 3
        y = idx % 3
        new_char = list(char)
        for dx,dy in d:
            nx = x + dx
            ny = y + dy
            tmp = new_char[:]
            if 0 <= nx < 3 and 0 <= ny < 3:
                next_idx = nx*3 + ny
                tmp[next_idx], tmp[idx] = tmp[idx],tmp[next_idx]
                tmp = ''.join(tmp)
                if not dist.get(tmp):
                    dist[tmp] = dist[char] + 1
                    dq.append(tmp)
    return -1

num = ""
for _ in range(3):
    arr = list(map(str,input().split()))
    num += ''.join(arr)
dist = {}
dist[num] = 0
print(BFS(num))


'''
1 2 3
4 5 6
7 8 0

6 4 7
8 5 0
3 2 1
'''
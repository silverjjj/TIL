
'''
8 3 12
9 1 6 7 5 4 6 7
9 5 1 8 8 3 5 8
5 2 6 8 6 9 2 1
9 2 1 8 7 5 2 3
6 5 5 1 4 5 7 2
1 7 1 8 1 9 5 5
6 2 2 9 2 5 1 4
7 1 1 2 5 9 5 7


4 2 13
6 1 9 7
9 8 5 8
3 4 5 3
8 2 6 7
'''


def subset(k, sum_num, total,com):
    global visited,maxV
    if sum_num > maxc:  # 가지치기
        return
    if k == m:  # 목표도달
        if sum_num <= maxc:
            if com > maxV:
                maxV = com
        return
    else:
        visited[k] = 1
        subset(k + 1, sum_num + total[k], total,com+(total[k]**2))
        visited[k] = 0
        subset(k + 1, sum_num, total, com)

def find(rm,c,st):
    total = []
    if c == n:
        return
    for j in st:
        total.append(rm[c][j])
    com = 0
    if sum(total) <= maxc:
        for l in st:
            com += (rm[c][l]**2)
    else: #  total > maxc:
        # 부분집합구하
        subset(0,0,total,0)
        com = maxV
    result.append(com)
    find(rm,c+1,st)

n,m,maxc = map(int,input().split())
rm = [list(map(int,input().split())) for _ in range(n)]
used = [0]*m
# n에서 m개
maxV = 0
visited = [0]*m
arr = [num for num in range(n)]
st = [num for num in range(-1,m-1)]
result = []
for _ in range(n-2):
    for j in range(m):
        st[j]+=1
    find(rm,0,st)
result = sorted(result)
last = result[-1]+result[-2]
print(last)
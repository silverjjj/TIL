# mst 푸는 문제는 kruskal or prim으로 풀자!!
# kruskal의 시간복잡도는 간선의 갯수
# 간선이 많을경우 prim이 유리

# make_set : 모든 정점에 대해 집합 생성
def make_set(x):
    p[x] = x

# 대표자를 찾는 함수(== 같은 집합인지를 알아보는 함수)
def find_set(x):
    if p[x] == x:
        return x
    else:
        p[x] = find_set(p[x])
        return p[x]

# x,y 두 함수를 합칠경우 x,y중 대표를 찾은뒤 랭크가 큰쪽이 부모가 되는거
def union(x, y):
    px = find_set(x)
    py = find_set(y)
    if rank[px] > rank[py]:  # 대표가 px
        p[py] = px
    else:
        p[px] = py  # 대표가 py
        if rank[py] == rank[py]:  # 랭크가 같으면 py의 랭크를 +=1 해준다
            rank[py] += 1

V, E = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(E)]

# 간선을 간선의 가중치기준으로 정렬
edges.sort(key=lambda x: x[2])

p = [0] * V     # 대표가 있는 배열
rank = [0] * V  # tree의 높이를 저장하는 배열

# 모든 정점에 대해 집합을 만든다
for i in range(V):
    make_set(i)

result = 0
mst = []  # 최소 가중치를 위한 경로를 저장
cnt = 0
# 모든 간선에 대해서 반복 -> V-1개의 간선이 선택될때까지
for i in range(E):
    # s:시작점, e:도착점, c:가중치
    s, e, c = edges[i][0], edges[i][1], edges[i][2]
     ##############################################################
    # 사이클이 아닐때만 간선을 선택
    # =>kruskal 알고리즘의 목표는 사이클을 돌지 않고 최단거리로 이동하는것
    # 사이클이 같을경우는 대표자가 같을경우와 같은말임
    # 대표자가 같을 경우를 찾기위해 find_set 함수를 통해 대표자를 찾는다.
    ##############################################################

    if find_set(s) == find_set(e):
        # 같을경우 continue하여 for문으로
        continue

    # 간선이 사이클이 아닐경우(== 두 정점의 대표가 다르다면)
    # => mst에 간선정보 더하기/ 두 정점을 합친다 => union
    result += c
    mst.append(edges[i])
    union(s, e)  # 두 간선집합이 사이클이 아닐때 => union함수를 통해 합쳐준다
    cnt += 1
    if cnt == V - 1: break

print(mst)
print(result)
'''
입력
7 11
0 5 60
0 1 32
0 2 31
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
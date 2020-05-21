def make_set(x):    # 초기 세팅을 위한 make 함수
    p[x] = x

def find_set(x):    # 대표자를 찾는 find 함수
    if p[x] == x: return x
    else:
        p[x] = find_set(p[x])
        return p[x]

def union(x,y):     # x집합과 y집합을 합치는 함수
    px = find_set(x)    # x와 y 둘다 대표자를 찾아옴
    py = find_set(y)
    if rank[px] > rank[py]:
        p[py] = px
    else:   # 같거나 작을때,
        p[px] = py  # py의 rank가 클경우
        if rank[px] == rank[py]:
            rank[py] +=1

T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    p = [0]*(n+1)
    rank = [0]*(n+1)
    for k in range(1,n+1):
        make_set(k)
    for l in range(len(arr)//2):
        i,j = arr[l*2], arr[(l*2)+1]
        union(i,j)
    result = set()
    for j in range(1, 1 + n):
        result.add(find_set(j))
        # print(result)
    print("#{} {}".format(tc, len(result)))
def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] == x: return x  # 나 == 부모가 같으면 리턴
    else: return find_set(p[x])    # 그게 아니라면 대표를 찾기위해 재귀

def union(x,y):
    # x집합 대표자, y집합 대표자를 찾음
    # x의 대표자가 y의 대표자를 가리키도록
    p[find_set(y)] = find_set(x)

N = 6
p = [0] * (N+1)
for i in range(1,N+1):
    make_set(i)
union(1,3)
# [0,1,2,1,4,5,6]
union(2,3)
# [0,2,2,1,4,5,6]
union(5,6)
# [0,2,2,1,4,5,5]
print(p)
print(find_set(6))
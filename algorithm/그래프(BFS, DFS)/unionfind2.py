# Path compression
def make_set(x):
    p[x] = x
def find_set(x):
    if p[x] == x: return x
    else:
        p[x] = find_set(p[x])
        return p[x]

def union(x,y): # y가 부모 x가 자식노드로
    px = find_set(x)
    py = find_set(y)
    if rank[px] > rank[py]:
        p[py] = px
    else:
        p[px] = py  
        if rank[px] == rank[py]:
            rank[py] +=1

N = 8
p = [0] * (N+1)
rank = [0] * (N+1)
for i in range(1,N+1):
    make_set(i)
print('p : ',p)
print('raxk : ', rank)
union(1,3)
print('p : ',p)
print('raxk : ', rank)
union(2,3)
print('p : ',p)
print('raxk : ', rank)
union(5,6)
print('p : ',p)
print('raxk : ', rank)
union(6,8)
print('p : ',p)
print('raxk : ', rank)
union(1,5)
print('p : ',p)
print('raxk : ', rank)
union(6,7)
print('p : ',p)
print('raxk : ', rank)
print(find_set(4))
print(find_set(5))
print(find_set(1))
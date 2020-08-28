# 노드번호가 1~13까지를  의미
# 부모노드 자식노드 순
'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

# v 는 노드수, e는 간선수
V = int(input())
E = V - 1
arr = list(map(int,input().split()))
# 1차배열로해보자
L = [0]* (V+1)  #왼쪽자식
R = [0]* (V+1)  #오른쪽자식
P = [0]* (V+1)  #부모

for i in range(0,len(arr),2):
    parent,child = arr[i],arr[i+1]
    if L[parent]:       # 0이 아니면
        R[parent] = child
    else:
        L[parent] = child
    P[child] = parent
print(P)
print(L)
print(R)
def inorder(v):  #방문하는 노드번호
    if v == 0: return

    # 전위 : 부모부터 시작해서 왼쪽먼저쫙~
    # print(v,end=" ")
    inorder(L[v])

    # 중위 : 왼쪽 -> 부모 -> 오른쪽
    # print(v, end=" ")

    inorder(R[v])

    # 후위: 왼 -> 오른 -> 부모
    print(v, end=" ")

# 시작을 1부터한다.
inorder(1)




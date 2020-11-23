'''
BOJ9934
input : 중위순회
'''
'''
완전이진트리
2 ^ 10 - 1 = 1023개의노드

4
8 4 9 2 10 5 11 1 12 6 13 3 14 7 15


'''
def traversal(depth):
    global dist
    if depth == -1:
        return
    tmp = []
    for cur in dist[-1]:
        tmp.append(cur - (2**depth))
        tmp.append(cur + (2**depth))
    dist.append(tmp)
    traversal(depth-1)

N = int(input())
arr = list(map(int,input().split()))
dist = []
L = len(arr)
dist.append([L//2])
traversal(N-2)
for row in dist:
    for num in row:
        print(arr[num],end =" ")
    print()
'''
5639
클래스를 활용하여 트리를 만들어서 풀면 시간초과발생

'''

import sys
input = sys.stdin.readline
def postorder(arr):
    global ans
    if len(arr) == 0:
        return
    if len(arr) == 1:
        ans.append(arr[0])
        return
    cur = arr[0]
    ans.append(cur)
    flag = True
    for idx,next in enumerate(arr[1:]):
        if cur < next:
            # print(next,idx+1)
            flag = False
            postorder(arr[idx+1:])
            postorder(arr[1:idx+1])
            break
    if flag:
        for num in arr[1:]:
            ans.append(num)

flag = True
arr = []
while flag:
    try:
        num = int(input())
        arr.append(num)
    except:
        flag = False
ans = []
postorder(arr)
for i in range(len(ans)-1,-1,-1):
    print(ans[i])

# class로 이진트리를 만드는 방법
# import sys
# input = sys.stdin.readline
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#     def __str__(self):
#         return str(self.data)
#
# class binary_tree:
#     # 처음 들어오면 init으로 트리의 root를 설정
#     def __init__(self):
#         self.head = Node(None)
#
#     def insert(self, node):
#         if self.head.data == None:  # root 만들기
#             self.head.data = node
#         else:
#             self.addNode(self.head,node)
#
#     def addNode(self,cur,node):
#         if cur.data > node:
#             if cur.left == None:    # 비어있으면
#                 cur.left = Node(node)
#             else:                   # 이미 있으면 그 아래로
#                 self.addNode(cur.left,node)
#         elif cur.data < node:
#             if cur.right == None:    # 비어있으면
#                 cur.right = Node(node)
#             else:                   # 이미 있으면 그 아래로
#                 self.addNode(cur.right,node)
#
#     def PostFix(self,cur):
#         # print(cur.left,cur,cur.right)
#         if cur.left != None:
#             self.PostFix(cur.left)
#         if cur.right != None:
#             self.PostFix(cur.right)
#         print(cur)
#
# t = binary_tree()
# flag = True
# while flag:
#     try:
#         num = int(input())
#         t.insert(num)
#     except:
#         t.PostFix(t.head)
#         flag = False
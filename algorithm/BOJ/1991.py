class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)

class Binary_Tree:
    def __init__(self):
        self.root = None

    def make_Node(self, node, left_node, right_node):
        if self.root == None:
            self.root = node
        node.left = left_node
        node.right = right_node

    def preorder(self, node):
        print(node, end="")
        if not node.left  == None : self.preorder(node.left)
        if not node.right == None : self.preorder(node.right)
    def inorder (self, node):
        if not node.left  == None : self.inorder(node.left)
        print(node, end="")
        if not node.right == None : self.inorder(node.right)

    def postorder (self, node):
        if not node.left  == None : self.postorder(node.left)
        if not node.right == None : self.postorder(node.right)
        print(node, end="")

n = int(input())
t = Binary_Tree()
arr = []
node = []
dict = {}
dict['.'] = None
for _ in range(n):
    cur, left, right = map(str,input().split())
    dict[cur] = Node(cur)
    arr.append([cur, left, right])

for cur, left, right in arr: 
    t.make_Node(dict[cur], dict[left], dict[right])
t.preorder(t.root)
print()
t.inorder(t.root)
print()
t.postorder(t.root)